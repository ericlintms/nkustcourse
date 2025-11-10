# **Lesson 1: Quantitative Stock Screening with Python**

## **Slide 13: The Rules in Pandas Code**

```python
# Create boolean conditions
cond1 = df_latest['每股盈餘'] > 1  
cond2 = df_latest['流動比率'] > 1.5  
cond3 = df_latest['營業利益率'] > 0.05  
cond4 = df_latest['每股淨值(B)'] > 10

# Combine all conditions with & (AND)  
selected_df = df_latest[cond1 & cond2 & cond3 & cond4]
```
