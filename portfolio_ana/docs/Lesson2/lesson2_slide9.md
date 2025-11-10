# **Lesson 2: Qualitative Analysis with LLMs**

## **Slide 9: Step 2: RAG in Practice**

* **Retrieval:** For each stock in selected_stocks.csv, we re-load the *full* fin_data_smallset.csv and filter it.

```python
# For loop: for stock in selected_stocks...  
stock_history_df = full_fin_df[full_fin_df['公司'] == stock_code]
```

* **Augmentation:** We create a simple text summary of its trends.

```python
eps_data = stock_history_df['每股盈餘'].tail(8) # Get last 8 quarters  
eps_trend = ", ".join(eps_data.astype(str))  
history_summary = f"- Recent EPS Trend: {eps_trend}"
```
