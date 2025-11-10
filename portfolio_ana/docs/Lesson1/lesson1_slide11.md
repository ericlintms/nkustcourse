# **Lesson 1: Quantitative Stock Screening with Python**

## **Slide 11: Filter Part 1: Finding the "Latest" Data**

* Our data has *all* history (1986, 1987...). We only want the *most recent* row.  
* **Pandas Magic:**  
  1. Sort by date: .sort_values('年/月')  
  2. Keep only the *last* row for each company: .drop_duplicates(subset=['公司'], keep='last')

```python
df_sorted = df.sort_values(by=['公司', '年/月'])  
df_latest = df_sorted.drop_duplicates(subset=['公司'], keep='last')
```

* Now df_latest contains only one row per company: their most recent report.
