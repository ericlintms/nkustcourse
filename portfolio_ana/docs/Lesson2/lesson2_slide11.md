# **Lesson 2: Qualitative Analysis with LLMs**

## **Slide 11: Our Prompt Structure**

**1. System Prompt:**

"You are a professional financial analyst for Taiwanese stocks. Be objective, professional, and use Traditional Chinese."

**2. Context (Data from RAG):**

"Here is the historical financial summary for {Stock Name}:

* Recent EPS Trend: 1.7, 3.0, 3.5, 3.1  
* Recent Op. Margin Trend: 5%, 7%, 8%, 6%  
* Recent Current Ratio Trend: 1.8, 1.9, 1.8, 2.0"

**3. User Query (Task):**

"Based *only* on this data, please analyze this company's:

1. Main Strengths (Pros)  
2. Potential Risks (Cons)  
3. A final rating (e.g., Buy, Hold, Sell) and your reasoning."
