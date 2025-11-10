# **Introduction to LLMs for Finance**

## **Slide 1: Title Page**

**From Python to LLMs: A Modern Workflow for Financial Analysis**

* **Course:** \[Portfolio Analysis with AI\]  
* **Instructor:** \[Eric Lin\]  
* **Date:** \[2025/11/17 , 2025/11/24\]

## **Slide 2: What is an LLM?**

* **LLM \= Large Language Model**  
* It's a powerful AI model trained on a massive amount of text data (like the entire internet).  
* **Core Abilities:**  
  * Understanding and generating human language.  
  * Summarizing long documents.  
  * Translating languages.  
  * Answering complex questions.  
  * Writing code.  
* **Think of it as...** a highly advanced autocomplete or a conversational partner that has read (almost) everything.

## **Slide 3: Key Terminology (Part 1\)**

* **Prompt:** The instruction or question you give to the LLM.  
  * *Prompt engineering* is the art of writing good prompts to get good answers.  
* **Token:** The basic unit of text for an LLM (roughly a word or part of a word).  
  * "Financial analysis" might be 2 or 3 tokens.  
  * Model context windows (e.g., 8K, 128K) are measured in tokens.  
* **Model:** The specific "brain" you are talking to (e.g., llama3, gpt-4, mistral).  
* **Hallucination:** When the LLM confidently states incorrect or fabricated "facts." It's a major risk we must manage.

## **Slide 4: Key Terminology (Part 2\)**

* **API (Application Programming Interface):** A "menu" that lets one computer program (our Python script) talk to another (the LLM).  
* **Cloud LLM:** The model runs on someone else's powerful computer (e.g., OpenAI, Google). You pay per use.  
* **Local LLM (Our Focus):** The model runs entirely on *your* own computer.  
  * **Tool:** We will use **Ollama** to serve a local model.  
  * **Pros:** Free, private (your data never leaves your machine).  
  * **Cons:** Requires a good computer (GPU), may be slower.

## **Slide 5: Why Combine Python with LLMs?**

Python and LLMs have opposite strengths, making them a perfect team.

| Task | Python (Pandas) | LLM (e.g., Llama 3\) |
| :---- | :---- | :---- |
| **Data Processing** | **Excellent** | **Poor** |
| **Math & Logic** | **Perfect** | **Good, but can fail** |
| **Speed (Numbers)** | **Very Fast** | **Very Slow** |
| **Language** | **Poor** (Basic strings) | **Excellent** |
| **Summarization** | **Impossible** | **Excellent** |
| **Context/Nuance** | **None** | **Good** |

Python (Quant) finds WHAT is interesting.  
LLM (Qual) explains WHY it's interesting.

## **Slide 6: Our Two-Lesson Workflow**

This is the core idea for our course.

### **Lesson 1: Quantitative (Quant) Screening**

* **Goal:** Use Python \+ Pandas to filter 100s of data points down to a few interesting stocks.  
* **Input:** fin\_data\_smallset.csv  
* **Process:** Hard-coded financial rules (EPS \> 1, Current Ratio \> 1.5)  
* **Output:** selected\_stocks.csv (A small list of stock codes)

### **Lesson 2: Qualitative (Qual) Analysis**

* **Goal:** Use an LLM to perform a deep analysis *only* on the stocks we selected.  
* **Input:** selected\_stocks.csv \+ fin\_data\_smallset.csv  
* **Process:** RAG (Retrieval-Augmented Generation)  
* **Output:** A human-readable report (Pros, Cons, Recommendation) for each stock.