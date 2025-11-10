# **Lesson 1: Quantitative Stock Screening with Python**

## **Slide 6: Step 1: Load & Clean the Data**

* "Data Janitor Work" - This is 80% of any data analysis job.  
* **Our Tasks:**  
  1. Load the CSV: pd.read_csv()  
  2. Fix column names: df.columns = df.columns.str.strip()  
  3. Convert text-numbers to *real numbers*: pd.to_numeric(..., errors='coerce')  
  * errors='coerce' is key: it turns any text that *isn't* a number (like '.') into NaN (Not a Number), which we can handle.
