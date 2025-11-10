# **Lesson 2: Qualitative Analysis with LLMs**

## **Slide 12: Step 4: Putting It All Together**

* Our llm_analyzer.py script becomes a simple loop:  
  1. Read selected_stocks.csv.  
  2. for each stock in the list:  
  3. **Retrieve** its history from fin_data_smallset.csv.  
  4. **Augment** a prompt with a summary of that history.  
  5. **Generate** an analysis by sending the prompt to the Ollama API.  
  6. Print the LLM's response.  
  7. Repeat.
