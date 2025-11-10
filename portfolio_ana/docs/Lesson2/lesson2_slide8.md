# **Lesson 2: Qualitative Analysis with LLMs**

## **Slide 8: RAG Explained Visually**

1. **User Query:** "Analyze stock 1101"  
2. **Our Code (Retrieval):**  
   * *Retrieves* all historical data for '1101' from fin_data_smallset.csv.  
3. **Our Code (Augmentation):**  
   * *Creates a summary* of that data (e.g., "EPS Trend: 1.2, 1.5, 1.3...").  
   * *Augments (inserts)* this summary into the prompt.  
4. **LLM (Generation):**  
   * Receives the full prompt: "Analyze stock 1101. Here is its data: [Data Summary...]"  
   * *Generates* the analysis based *only* on the data we provided.
