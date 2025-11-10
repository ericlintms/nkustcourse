# **Introduction to LLMs for Finance**

## **Slide 6: Our Two-Lesson Workflow**

This is the core idea for our course.

### **Lesson 1: Quantitative (Quant) Screening**

* **Goal:** Use Python + Pandas to filter 100s of data points down to a few interesting stocks.  
* **Input:** fin_data_smallset.csv  
* **Process:** Hard-coded financial rules (EPS > 1, Current Ratio > 1.5)  
* **Output:** selected_stocks.csv (A small list of stock codes)

### **Lesson 2: Qualitative (Qual) Analysis**

* **Goal:** Use an LLM to perform a deep analysis *only* on the stocks we selected.  
* **Input:** selected_stocks.csv + fin_data_smallset.csv  
* **Process:** RAG (Retrieval-Augmented Generation)  
* **Output:** A human-readable report (Pros, Cons, Recommendation) for each stock.
