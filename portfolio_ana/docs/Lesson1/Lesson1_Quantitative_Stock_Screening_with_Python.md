# **Lesson 1: Quantitative Stock Screening with Python**

## **Slide 1: Title Page**

**Lesson 1: Quantitative Stock Screening with Python**

* Finding the "Needle in a Haystack" with Pandas

## **Slide 2: Recap: Our Two-Lesson Goal**

1. **Lesson 1 (Today):** Use **Python** for **Quantitative Screening**.  
   * *Fast, objective, data-driven.*  
   * Filter from many \-\> few.  
2. **Lesson 2 (Next Time):** Use **LLM** for **Qualitative Analysis**.  
   * *Slow, subjective, context-aware.*  
   * Analyze from few \-\> deep insights.

## **Slide 3: Today's Objective**

**To build a Python script (stock\_screener.py) that:**

1. Loads our messy financial data.  
2. Cleans and transforms it.  
3. Calculates new financial ratios.  
4. Applies a set of "buy" rules (our filter).  
5. Saves the result for Lesson 2\.

## **Slide 4: Our Main Toolbox: Pandas**

* **Pandas** is the most popular library in Python for data analysis.  
* It gives us a powerful tool called the **DataFrame**.  
* **DataFrame \=** A smart spreadsheet (like Excel) that you can control with code.  
* We will use it for everything today.

## **Slide 5: The Data: fin\_data\_smallset.csv**

* **Format:** CSV (Comma-Separated Values)  
* **Content:** Historical financial statements for multiple companies.  
* **Columns:** 283+ (e.g., 公司 (Code), 簡稱 (Name), 每股盈餘 (EPS), 流動資 Antworten (Current Assets))  
* **Problem:** This data is **NOT** clean.  
  * Column names have spaces (' 簡稱').  
  * Numbers are stored as text ('1.5' vs. '.').  
  * We have data from 1986, but we only want the *latest* data.

## **Slide 6: Step 1: Load & Clean the Data**

* "Data Janitor Work" \- This is 80% of any data analysis job.  
* **Our Tasks:**  
  1. Load the CSV: pd.read\_csv()  
  2. Fix column names: df.columns \= df.columns.str.strip()  
  3. Convert text-numbers to *real numbers*: pd.to\_numeric(..., errors='coerce')  
  * errors='coerce' is key: it turns any text that *isn't* a number (like '.') into NaN (Not a Number), which we can handle.

## **Slide 7: Step 2: Define Our "Why" (Financial Metrics)**

* We need rules for our screener.  
* **CRITICAL LIMITATION:** Our dataset has **NO STOCK PRICE** data.  
* Therefore, we **cannot** calculate common ratios like:  
  * P/E Ratio (Price-to-Earnings)  
  * P/B Ratio (Price-to-Book)  
* **Solution:** We will use **fundamentals-only** metrics.

## **Slide 8: Our Fundamental-Only Metrics**

1. **Profitability:** Is it making money?  
   * **Metric:** 每股盈餘 (EPS)  
   * **Source:** Direct from data.  
2. **Liquidity (Solvency):** Can it pay its short-term bills?  
   * **Metric:** Current Ratio  
   * **Formula:** 流動資產 (Current Assets) / 流動負債 (Current Liabilities)  
3. **Efficiency:** Is its main business profitable?  
   * **Metric:** Operating Margin  
   * **Formula:** 營業利益 (Operating Income) / 營業收入淨額 (Net Revenue)  
4. **Value (Solidity):** What is the company's "book" value?  
   * **Metric:** 每股淨值(B) (Book Value Per Share)  
   * **Source:** Direct from data.

## **Slide 9: Step 3: Feature Engineering**

* "Feature Engineering" is just a fancy term for creating new columns (like Current Ratio) from existing columns.  
* In Pandas, this is easy:

\# 1\. Calculate Current Ratio  
df\['流動比率'\] \= df\['流動資產'\] / df\['流動負債'\]

\# 2\. Calculate Operating Margin  
df\['營業利益率'\] \= df\['營業利益'\] / df\['營業收入淨額'\]

* **Risk:** We must handle "Divide by Zero" errors\! (e.g., if Revenue is 0).

## **Slide 10: Step 4: The Screener (Filtering)**

* We have all our data and metrics. Now we filter.  
* **Two-Part Filter:**  
  1. Get the **latest financial report** for *each* company.  
  2. Apply our **financial rules** to that latest report.

## **Slide 11: Filter Part 1: Finding the "Latest" Data**

* Our data has *all* history (1986, 1987...). We only want the *most recent* row.  
* **Pandas Magic:**  
  1. Sort by date: .sort\_values('年/月')  
  2. Keep only the *last* row for each company: .drop\_duplicates(subset=\['公司'\], keep='last')

df\_sorted \= df.sort\_values(by=\['公司', '年/月'\])  
df\_latest \= df\_sorted.drop\_duplicates(subset=\['公司'\], keep='last')

* Now df\_latest contains only one row per company: their most recent report.

## **Slide 12: Filter Part 2: Applying Our Rules**

* This is the core of our "Quant" logic.  
* **Our Rules:**  
  1. EPS \> 1 (Profitable)  
  2. Current Ratio \> 1.5 (Safe, can pay bills)  
  3. Operating Margin \> 0.05 (5%) (Efficient core business)  
  4. BVPS \> 10 (Solid book value)

## **Slide 13: The Rules in Pandas Code**

\# Create boolean conditions  
cond1 \= df\_latest\['每股盈餘'\] \> 1  
cond2 \= df\_latest\['流動比率'\] \> 1.5  
cond3 \= df\_latest\['營業利益率'\] \> 0.05  
cond4 \= df\_latest\['每股淨值(B)'\] \> 10

\# Combine all conditions with & (AND)  
selected\_df \= df\_latest\[cond1 & cond2 & cond3 & cond4\]

## **Slide 14: Step 5: Save the Results**

* We now have selected\_df, a tiny DataFrame with maybe 2-3 stocks.  
* This is our "Needle in the Haystack."  
* We save it to a new file, which will be the input for Lesson 2\.

output\_file \= "selected\_stocks.csv"  
selected\_df.to\_csv(output\_file, index=False, encoding='utf-8-sig')

## **Slide 15: Lesson 1 Review**

* We started with a large, messy CSV.  
* We used **Pandas** to **Clean** data.  
* We **Engineered** new metrics (Current Ratio, Op. Margin).  
* We **Filtered** for the latest data.  
* We **Screened** for stocks matching our rules.  
* **Result:** A short, clean list of *quantitatively* interesting stocks.

**Next Time:** We find out *why* they are interesting.