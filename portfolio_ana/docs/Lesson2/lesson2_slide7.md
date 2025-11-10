# **Lesson 2: Qualitative Analysis with LLMs**

## **Slide 7: The Solution: RAG**

* **RAG = Retrieval-Augmented Generation**  
* It's the most important concept for using LLMs with private data.  
* **The Idea:** Don't *ask* the LLM a question it can't answer. *Give* it the data it needs *inside the prompt* and ask it to summarize.

**Analogy:**

* **Bad Prompt (No RAG):** "Hey, what's on page 5 of the book in my backpack?" (LLM: "I can't see your backpack.")  
* **Good Prompt (RAG):** "Here is the text from page 5: [...text...]. Please summarize it for me." (LLM: "Certainly!")
