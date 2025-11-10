import pandas as pd
import numpy as np
import time

# --- 設定 ---
INPUT_PATH = "data/financial_data_full.csv"
OUTPUT_PATH = "data/financial_data_full_cleaned.csv"

def clean_financial_data(filepath):
    """
    清理財務資料，邏輯同步於 llm_analyzer.py
    """
    try:
        print(f"正在讀取 {filepath}...")
        df = pd.read_csv(filepath, na_values='.')
        print(f"✓ 檔案讀取完成，總行數：{len(df)}")
    except Exception as e:
        print(f"讀取 {filepath} 失敗: {e}")
        return None
    
    # 清理欄位名稱（去除前後空白）
    df.columns = df.columns.str.strip()
    print(f"✓ 欄位名稱已清理")
    
    # 清理所有文字欄位的空白
    print("正在清理文字欄位的空白...")
    for col in df.columns:
        if df[col].dtype == 'object':  # 文字欄位
            df[col] = df[col].str.strip() if df[col].dtype == 'object' else df[col]
    print(f"✓ 文字欄位空白已清理")
    
    # 定義需要轉換為數值的欄位
    numeric_cols = ['每股盈餘', '流動資產', '流動負債', '每股�淨值(B)', '營業利益', '營業收入淨額']
    
    # 轉換數值欄位
    print("正在轉換數值欄位...")
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            print(f"  └─ {col}")
        else:
            print(f"  └─ {col} (未找到)")
    
    # 計算營業利益率
    if '營業收入淨額' in df.columns and '營業利益' in df.columns:
        print("正在計算營業利益率...")
        df['營業利益率'] = df.apply(
            lambda row: row['營業利益'] / row['營業收入淨額'] if row['營業收入淨額'] != 0 else np.nan,
            axis=1
        )
        print("✓ 營業利益率計算完成")
    
    # 計算流動比率
    if '流動資產' in df.columns and '流動負債' in df.columns:
        print("正在計算流動比率...")
        df['流動比率'] = df.apply(
            lambda row: row['流動資產'] / row['流動負債'] if row['流動負債'] != 0 else np.nan,
            axis=1
        )
        print("✓ 流動比率計算完成")
    
    return df

# --- 主程式執行 ---
if __name__ == "__main__":
    print("="*60)
    print("財務資料清理程式")
    print("="*60)
    
    start_time = time.time()
    
    # 清理資料
    print(f"\n開始清理 {INPUT_PATH}...\n")
    cleaned_df = clean_financial_data(INPUT_PATH)
    
    if cleaned_df is None:
        print("資料清理失敗，程式終止。")
        exit()
    
    # 儲存清理後的資料
    print(f"\n正在保存清理後的資料至 {OUTPUT_PATH}...")
    try:
        cleaned_df.to_csv(OUTPUT_PATH, index=False, encoding='utf-8-sig')
        print(f"✓ 資料已保存")
    except Exception as e:
        print(f"保存失敗: {e}")
        exit()
    
    # 統計資訊
    print("\n" + "="*60)
    print("清理統計")
    print("="*60)
    print(f"原始資料行數: {len(cleaned_df)}")
    print(f"總欄位數: {len(cleaned_df.columns)}")
    print(f"欄位列表: {', '.join(cleaned_df.columns.tolist())}")
    
    # 顯示各欄位的非空值統計
    print(f"\n欄位非空值統計:")
    for col in cleaned_df.columns:
        non_null_count = cleaned_df[col].notna().sum()
        null_count = cleaned_df[col].isna().sum()
        print(f"  └─ {col}: {non_null_count} 筆非空值, {null_count} 筆空值")
    
    elapsed = time.time() - start_time
    print("\n" + "="*60)
    print(f"✓ 清理完成！耗時：{elapsed:.2f} 秒")
    print("="*60)
