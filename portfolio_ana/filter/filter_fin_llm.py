#!/usr/bin/env python3
"""
財務資料欄位過濾程式

目的：從完整的 financial_data_full_cleaned.csv 中篩選出
      stock_screener.py 和 llm_analyzer.py 所需的關鍵欄位，
      同時保留一些專業財務分析常用的欄位，以減少檔案大小。

使用方式：
    python filter/filter_fin_llm.py

輸出檔案：
    data/filtered_data.csv
"""

import pandas as pd
import os


def filter_financial_data(input_file, output_file):
    """
    從完整財務資料中篩選出必要欄位
    
    Args:
        input_file (str): 輸入檔案路徑 (financial_data_full_cleaned.csv)
        output_file (str): 輸出檔案路徑 (filtered_data.csv)
    """
    
    print(f"正在載入資料：{input_file}")
    
    # 讀取完整資料
    try:
        df = pd.read_csv(input_file)
        print(f"✓ 成功載入資料，共 {len(df)} 筆記錄，{len(df.columns)} 個欄位")
    except FileNotFoundError:
        print(f"錯誤：找不到檔案 {input_file}")
        return False
    except Exception as e:
        print(f"錯誤：讀取檔案失敗 - {e}")
        return False
    
    # 定義需要保留的欄位
    # 1. 基本識別欄位
    basic_fields = [
        '公司',           # 公司代碼
        '簡稱',           # 公司簡稱
        '年/月',          # 財報期間
        '季別',           # 季別
        '合併(Y/N)',      # 是否為合併報表
    ]
    
    # 2. stock_screener.py 使用的欄位（必需）
    screener_fields = [
        '每股盈餘',       # 用於獲利能力篩選
        '流動資產',       # 用於計算流動比率
        '流動負債',       # 用於計算流動比率
        '每股淨值(B)',    # 用於公司體質篩選
        '營業利益',       # 用於計算營業利益率
        '營業收入淨額',   # 用於計算營業利益率
    ]
    
    # 3. 資產負債表關鍵欄位（財務分析常用）
    balance_sheet_fields = [
        '資產總額',       # 總資產規模
        '負債總額',       # 總負債
        '股東權益總額',   # 淨值
        '現金及約當現金', # 現金部位
        '存貨',           # 存貨水準
        '應收帳款及票據', # 應收帳款
        '短期借款',       # 短期負債
        '普通股股本',     # 股本
    ]
    
    # 4. 損益表關鍵欄位
    income_statement_fields = [
        '營業成本',       # 成本結構
        '營業毛利',       # 毛利
        '營業費用',       # 營業費用
        '稅前淨利',       # 稅前盈餘
        '所得稅費用',     # 所得稅
        '合併總損益',     # 淨利（稅後）
    ]
    
    # 5. 現金流量表關鍵欄位
    cash_flow_fields = [
        '來自營運之現金流量',  # 營業現金流
        '投資活動之現金流量',  # 投資現金流
        '籌資活動之現金流量',  # 融資現金流
    ]
    
    # 6. 財務比率關鍵欄位（部分可能需要計算）
    ratio_fields = [
        'ROE(A)－稅後',   # 股東權益報酬率
        'ROA(A)稅後息前', # 資產報酬率
        '負債比率',       # 負債比率
        '速動比率',       # 速動比率
        '營業毛利率',     # 毛利率
        '營業利益率',     # 營業利益率
        '稅後淨利率',     # 淨利率
        '流動比率',       # 流動比率
    ]
    
    # 7. 每股相關指標
    per_share_fields = [
        '每股現金流量',   # 每股營業現金流
        '每股營業額',     # 每股營收
        '每股營業利益',   # 每股營業利益
        '每股稅前淨利',   # 每股稅前盈餘
    ]
    
    # 8. 成長性指標
    growth_fields = [
        '營收成長率',     # 營收成長率
        '營業利益成長率', # 營業利益成長率
        '稅後淨利成長率', # 淨利成長率
        '總資產成長率',   # 資產成長率
    ]
    
    # 9. 產業與市場分類
    classification_fields = [
        '市場別',              # 上市/上櫃
        'TEJ主產業代碼',       # 產業分類
        'TEJ子產業代碼',       # 子產業分類
    ]
    
    # 合併所有需要的欄位
    required_fields = (
        basic_fields + 
        screener_fields + 
        balance_sheet_fields + 
        income_statement_fields + 
        cash_flow_fields + 
        ratio_fields + 
        per_share_fields + 
        growth_fields + 
        classification_fields
    )
    
    # 去除重複欄位
    required_fields = list(dict.fromkeys(required_fields))
    
    # 檢查哪些欄位存在於原始資料中
    available_fields = [field for field in required_fields if field in df.columns]
    missing_fields = [field for field in required_fields if field not in df.columns]
    
    print(f"\n欄位統計：")
    print(f"  - 需要的欄位數：{len(required_fields)}")
    print(f"  - 實際存在的欄位數：{len(available_fields)}")
    print(f"  - 缺失的欄位數：{len(missing_fields)}")
    
    if missing_fields:
        print(f"\n警告：以下欄位在原始資料中不存在（將被跳過）：")
        for field in missing_fields:
            print(f"  - {field}")
    
    # 篩選資料
    print(f"\n正在篩選欄位...")
    filtered_df = df[available_fields].copy()
    
    # 顯示資料大小變化
    original_size = df.memory_usage(deep=True).sum() / (1024 ** 2)  # MB
    filtered_size = filtered_df.memory_usage(deep=True).sum() / (1024 ** 2)  # MB
    reduction_pct = (1 - filtered_size / original_size) * 100
    
    print(f"\n資料大小變化：")
    print(f"  - 原始資料：{original_size:.2f} MB ({len(df.columns)} 欄位)")
    print(f"  - 篩選後：{filtered_size:.2f} MB ({len(filtered_df.columns)} 欄位)")
    print(f"  - 減少：{reduction_pct:.1f}%")
    
    # 確保輸出目錄存在
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"\n✓ 已建立輸出目錄：{output_dir}")
    
    # 儲存篩選後的資料
    print(f"\n正在儲存至：{output_file}")
    try:
        filtered_df.to_csv(output_file, index=False, encoding='utf-8-sig')
        
        # 檢查檔案大小
        file_size = os.path.getsize(output_file) / (1024 ** 2)  # MB
        print(f"✓ 成功儲存！檔案大小：{file_size:.2f} MB")
        print(f"✓ 共保留 {len(filtered_df)} 筆記錄，{len(filtered_df.columns)} 個欄位")
        
        return True
        
    except Exception as e:
        print(f"錯誤：儲存檔案失敗 - {e}")
        return False


def main():
    """主程式"""
    
    # 設定輸入與輸出檔案路徑
    input_file = "data/financial_data_full_cleaned.csv"
    output_file = "data/filtered_data.csv"
    
    print("="*60)
    print("財務資料欄位過濾程式")
    print("="*60)
    print()
    
    # 執行過濾
    success = filter_financial_data(input_file, output_file)
    
    print()
    print("="*60)
    if success:
        print("✓ 過濾完成！")
        print()
        print("說明：")
        print(f"  - 篩選後的資料已儲存至：{output_file}")
        print(f"  - 可用於 stock_screener.py 和 llm_analyzer.py")
        print(f"  - 包含選股分析所需的所有關鍵欄位")
    else:
        print("✗ 過濾失敗，請檢查錯誤訊息")
    print("="*60)


if __name__ == "__main__":
    main()
