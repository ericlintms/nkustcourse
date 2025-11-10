import pandas as pd

def clean_financial_data(filepath="data/financial_data_filtered.csv"):
    """
    載入並清理財務資料檔案。
    """
    try:
        df = pd.read_csv(filepath, na_values='.')
    except FileNotFoundError:
        print(f"錯誤：找不到檔案 {filepath}")
        return None
    except Exception as e:
        print(f"讀取檔案時發生錯誤: {e}")
        return None
        
    # 1. 清理欄位名稱 (移除前後空白)
    df.columns = df.columns.str.strip()

    # 2. 定義需要轉換為數值的關鍵財務欄位
    # (基於資料檢視的結果)
    numeric_cols = [
        '每股盈餘', '流動資產', '流動負債', '每股淨值(B)',
        '營業利益', '營業收入淨額'
    ]
    
    # 確保欄位存在
    for col in numeric_cols:
        if col not in df.columns:
            print(f"警告：關鍵欄位 '{col}' 不在資料表中。跳過此欄位。")
            numeric_cols.remove(col)
            
    # 3. 轉換為數值型態，無法轉換的設為 NaN
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    return df

def screen_stocks(df: pd.DataFrame):
    """
    根據最新的財務數據進行股票篩選。
    """
    if df is None:
        return pd.DataFrame() # 回傳空的 DataFrame
        
    # 1. 計算財務比率 (確保分母不為零)
    # 流動比率 = 流動資產 / 流動負債
    df['流動比率'] = df['流動資產'] / df['流動負債']
    
    # 營業利益率 = 營業利益 / 營業收入淨額
    df['營業利益率'] = df['營業利益'] / df['營業收入淨額']
    
    # 2. 篩選最新的資料
    # 依公司代碼和年/月排序，確保 '年/月' 是可排序的 (假設其格式正確)
    df_sorted = df.sort_values(by=['公司', '年/月'])
    
    # 取得每家公司最新的(最後一筆)資料
    df_latest = df_sorted.drop_duplicates(subset=['公司'], keep='last')
    
    # 3. 設定篩選條件
    # 條件 1: 獲利能力 (EPS > 70)
    cond1 = df_latest['每股盈餘'] > 70
    
    # 條件 2: 償債能力 (流動比率 > 1.8)
    cond2 = df_latest['流動比率'] > 1.8
    
    # 條件 3: 本業獲利 (營業利益率 > 20%)
    cond3 = df_latest['營業利益率'] > 0.2
    
    # 條件 4: 公司體質 (每股淨值 > 100)
    cond4 = df_latest['每股淨值(B)'] > 100
    
    # 4. 應用所有條件
    selected_df = df_latest[cond1 & cond2 & cond3 & cond4]
    
    return selected_df[['公司', '簡稱', '年/月', '每股盈餘', '流動比率', '營業利益率', '每股淨值(B)']]

# --- 主程式執行 ---
if __name__ == "__main__":
    
    print("正在載入與清理資料...")
    filename = "data/financial_data_filtered.csv"
    main_df = clean_financial_data(filename)
    
    if main_df is not None:
        print("正在篩選股票...")
        selected_stocks = screen_stocks(main_df)
        
        print("\n--- 篩選結果 ---")
        if selected_stocks.empty:
            print("沒有找到符合所有條件的股票。")
            print("（提示：您可能需要放寬篩選條件，或檢查 'fin_data_smallset.csv' 的資料內容）")
        else:
            print(selected_stocks)
            
            # 5. 儲存結果
            output_file = "selected_stocks.csv"
            selected_stocks.to_csv(output_file, index=False, encoding='utf-8-sig')
            print(f"\n篩選結果已儲存至 {output_file}")

