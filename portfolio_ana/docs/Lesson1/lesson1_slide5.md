# **Lesson 1: Quantitative Stock Screening with Python**

## **Slide 5: The Data: fin_data_smallset.csv**

* **Format:** CSV (Comma-Separated Values)  
* **Content:** Historical financial statements for multiple companies.  
* **Columns:** 283+ (e.g., 公司 (Code), 簡稱 (Name), 每股盈餘 (EPS), 流動資 Antworten (Current Assets))  
* **Problem:** This data is **NOT** clean.  
  * Column names have spaces (' 簡稱').  
  * Numbers are stored as text ('1.5' vs. '.').  
  * We have data from 1986, but we only want the *latest* data.
