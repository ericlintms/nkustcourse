# **Lesson 1: Quantitative Stock Screening with Python**

## **Slide 9: Step 3: Feature Engineering**

* "Feature Engineering" is just a fancy term for creating new columns (like Current Ratio) from existing columns.  
* In Pandas, this is easy:

```python
# 1. Calculate Current Ratio
df['流動比率'] = df['流動資產'] / df['流動負債']

# 2. Calculate Operating Margin
df['營業利益率'] = df['營業利益'] / df['營業收入淨額']
```

* **Risk:** We must handle "Divide by Zero" errors! (e.g., if Revenue is 0).
