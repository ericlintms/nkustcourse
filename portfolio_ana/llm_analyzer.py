import pandas as pd
import requests
import time
import numpy as np

# --- 設定 ---
OLLAMA_URL = "http://163.18.46.187:22434/api/generate"
OLLAMA_MODEL = "gemma3:4b" # ! 請修改為您在 Ollama 下載的模型名稱
FIN_DATA_PATH = "data/financial_data_filtered.csv"
SELECTED_STOCKS_PATH = "selected_stocks.csv"

# --- 複製自 screener，確保資料處理邏輯一致 ---
def clean_financial_data(filepath):
    try:
        df = pd.read_csv(filepath, na_values='.')
    except Exception as e:
        print(f"讀取 {filepath} 失敗: {e}")
        return None
        
    df.columns = df.columns.str.strip()
    
    numeric_cols = ['每股盈餘', '流動資產', '流動負債', '每股淨值(B)', '營業利益', '營業收入淨額']
    
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
    if '營業收入淨額' in df.columns and '營業利益' in df.columns:
         # 處理除以零的情況
        df['營業利益率'] = df.apply(
            lambda row: row['營業利益'] / row['營業收入淨額'] if row['營業收入淨額'] != 0 else np.nan,
            axis=1
        )
    if '流動資產' in df.columns and '流動負債' in df.columns:
        df['流動比率'] = df.apply(
            lambda row: row['流動資產'] / row['流動負債'] if row['流動負債'] != 0 else np.nan,
            axis=1
        )
            
    return df

# --- LLM 溝通函式 ---
def get_llm_analysis(stock_name, stock_code, history_summary):
    """
    呼叫 Ollama API 取得個股分析。
    """
    
    system_prompt = (
        "你是一位專業的財務分析師，專長是分析台灣上市公司的基本面。"
        "請保持客觀、專業，並使用繁體中文回答。"
    )
    
    user_query = (
        f"請針對 {stock_name} ({stock_code}) 進行分析。\n\n"
        "我提供的歷史財務摘要如下：\n"
        f"{history_summary}\n\n"
        "請根據這份摘要，分析這間公司的：\n"
        "1. 主要優勢 (Pros)\n"
        "2. 潛在風險 (Cons)\n"
        "3. 綜合評價與持股建議 (例如：買進、持有、賣出)，並說明你的理由。"
    )
    
    # 結合 System Prompt 和 User Query (Ollama 的格式)
    # 注意：不同的模型可能對 Prompt 格式有不同偏好
    full_prompt = f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{user_query}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n"


    payload = {
        "model": OLLAMA_MODEL,
        "prompt": full_prompt,
        "stream": False # 我們希望一次性收到完整回應
    }
    
    print(f"正在向 Ollama 請求分析： {stock_name}...")
    
    try:
        start_time = time.time()
        response = requests.post(OLLAMA_URL, json=payload, timeout=300) # 延長超時時間
        elapsed_time = time.time() - start_time
        response.raise_for_status() # 如果發生 HTTP 錯誤，拋出例外
        
        print(f"✓ Ollama 回應耗時：{elapsed_time:.2f} 秒")
        
        # 解析 Ollama 回應
        response_data = response.json()
        analysis = response_data.get("response", "錯誤：Ollama 回應中沒有 'response' 欄位。")
        
        return analysis.strip()
        
    except requests.exceptions.ConnectionError:
        return f"錯誤：無法連線至 Ollama ({OLLAMA_URL})。請確認 Ollama 服務正在運行。"
    except requests.exceptions.Timeout:
        return "錯誤：Ollama 回應超時。"
    except requests.exceptions.RequestException as e:
        return f"錯誤：API 請求失敗: {e}"

# --- 主程式執行 ---
if __name__ == "__main__":
    
    # 記錄總開始時間
    total_start_time = time.time()
    
    # 1. 載入完整的財務資料庫 (用於撈取歷史資料)
    print(f"正在載入完整資料庫 {FIN_DATA_PATH}...")
    stage_start = time.time()
    full_fin_df = clean_financial_data(FIN_DATA_PATH)
    stage_elapsed = time.time() - stage_start
    print(f"✓ 資料庫載入完成，耗時：{stage_elapsed:.2f} 秒")
    
    if full_fin_df is None:
        exit()

    # 2. 載入篩選出的股票清單
    print("\n正在載入篩選出的股票清單...")
    stage_start = time.time()
    try:
        selected_df = pd.read_csv(SELECTED_STOCKS_PATH)
    except FileNotFoundError:
        print(f"錯誤：找不到 {SELECTED_STOCKS_PATH}。")
        print("請先執行 'stock_screener.py' 來產生選股清單。")
        exit()
    stage_elapsed = time.time() - stage_start
    print(f"✓ 股票清單載入完成，耗時：{stage_elapsed:.2f} 秒")
        
    if selected_df.empty:
        print("選股清單是空的，沒有股票需要分析。")
        exit()
        
    print(f"✓ 找到 {len(selected_df)} 支符合條件的股票，準備進行 LLM 分析...\n")

    # 3. 遍歷每支股票，進行分析
    for index, row in selected_df.iterrows():
        stock_start_time = time.time()
        stock_code = str(row['公司'])
        stock_name = row['簡稱']
        print(f"\n[{index + 1}/{len(selected_df)}] 開始處理 {stock_name} ({stock_code})")
        
        # 3.1 從完整資料庫中撈取該股票的 *所有* 歷史資料
        extract_start = time.time()
        stock_history_df = full_fin_df[full_fin_df['公司'] == row['公司']].sort_values('年/月')
        extract_elapsed = time.time() - extract_start
        
        if stock_history_df.empty:
            print(f"警告：在完整資料庫中找不到 {stock_name} ({stock_code}) 的歷史資料。")
            continue
            
        print(f"  └─ 歷史資料提取耗時：{extract_elapsed:.3f} 秒")
            
        # 3.2 建立 RAG 的「資料摘要」
        summary_start = time.time()
        summary_lines = []
        
        # 整理 EPS 趨勢
        eps_data = stock_history_df[['年/月', '每股盈餘']].dropna()
        eps_trend = [f"{r['年/月']}: {r['每股盈餘']:.2f}" for i, r in eps_data.tail(8).iterrows()] # 取近8筆
        summary_lines.append(f"- 近期 EPS (每股盈餘) 趨勢： {', '.join(eps_trend) or '無資料'}")

        # 整理營業利益率趨勢
        margin_data = stock_history_df[['年/月', '營業利益率']].dropna()
        margin_trend = [f"{r['年/月']}: {r['營業利益率']:.2%}" for i, r in margin_data.tail(8).iterrows()] # 取近8筆
        summary_lines.append(f"- 近期營業利益率趨勢： {', '.join(margin_trend) or '無資料'}")
        
        # 整理流動比率趨勢
        cr_data = stock_history_df[['年/月', '流動比率']].dropna()
        cr_trend = [f"{r['年/月']}: {r['流動比率']:.2f}" for i, r in cr_data.tail(8).iterrows()] # 取近8筆
        summary_lines.append(f"- 近期流動比率趨勢： {', '.join(cr_trend) or '無資料'}")

        # 整理每股淨值趨勢
        bvps_data = stock_history_df[['年/月', '每股淨值(B)']].dropna()
        bvps_trend = [f"{r['年/月']}: {r['每股淨值(B)']:.2f}" for i, r in bvps_data.tail(8).iterrows()] # 取近8筆
        summary_lines.append(f"- 近期每股淨值(B)趨勢： {', '.join(bvps_trend) or '無資料'}")

        history_summary_text = "\n".join(summary_lines)
        summary_elapsed = time.time() - summary_start
        print(f"  └─ 資料摘要準備耗時：{summary_elapsed:.3f} 秒")
        
        # 3.3 呼叫 LLM
        analysis_result = get_llm_analysis(stock_name, stock_code, history_summary_text)
        
        # 3.4 印出結果
        print("\n" + "="*50)
        print(f"  {stock_name} ({stock_code}) - LLM 分析報告")
        print("="*50)
        print(analysis_result)
        
        stock_elapsed = time.time() - stock_start_time
        print("="*50)
        print(f"✓ 該股票分析完成，耗時：{stock_elapsed:.2f} 秒\n")
    
    # 列印總耗時統計
    total_elapsed = time.time() - total_start_time
    print("\n" + "="*50)
    print(f"✓ 全部分析完成！")
    print(f"  總耗時：{total_elapsed:.2f} 秒 ({total_elapsed / 60:.2f} 分鐘)")
    print("="*50)
