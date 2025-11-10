# **Lesson 1: Quantitative Stock Screening with Python**

## **Slide 14: Step 5: Save the Results**

* We now have selected_df, a tiny DataFrame with maybe 2-3 stocks.  
* This is our "Needle in the Haystack."  
* We save it to a new file, which will be the input for Lesson 2.

```python
output_file = "selected_stocks.csv"  
selected_df.to_csv(output_file, index=False, encoding='utf-8-sig')
```
