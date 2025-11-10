# **Lesson 2: Qualitative Analysis with LLMs**

## **Slide 1: Title Page**

**Lesson 2: Qualitative Analysis with LLMs**

* From "What" to "Why" using Ollama and RAG

## **Slide 2: Recap: Where We Are**

* In Lesson 1, we built a **Quantitative Screener**.  
* We filtered a large fin\_data\_smallset.csv...  
* ...down to a small selected\_stocks.csv.  
* We found **WHAT** stocks meet our rules (e.g., EPS \> 1, Ratio \> 1.5).

## **Slide 3: Today's Objective**

* Today, we find out **WHY**.  
* **The Problem:** A stock with "EPS \> 1" could be:  
  * **A:** A great company on a growth trend.  
  * **B:** A terrible company that had one lucky quarter.  
* **Our Quant screen can't tell the difference.** A number is just a number.  
* We need **context**, **trends**, and **nuance**.  
* **Goal:** We will use an LLM to provide this qualitative analysis.

## **Slide 4: Our New Tool: Ollama**

* **Ollama** is a tool that lets us run powerful open-source LLMs (like llama3 or mistral) on our local machine.  
* It creates a simple API server at http://localhost:11434.  
* Our Python script can send a "prompt" to this server and get an "analysis" back.  
* **Key Benefit:** Our private financial data **never leaves our computer**. This is critical for data privacy.

## **Slide 5: Step 1: Connecting to Ollama**

* We use the requests library in Python.  
* We send an HTTP POST request to the Ollama API (/api/generate).  
* The payload is a JSON object containing our model and prompt.

import requests

payload \= {  
    "model": "llama3", \# Or whatever model you have  
    "prompt": "Why is the sky blue?",  
    "stream": False  
}

response \= requests.post(  
    "http://localhost:11434/api/generate",   
    json=payload  
)

print(response.json()\['response'\])

## **Slide 6: The Core Challenge of This Lesson**

* We have selected\_stocks.csv (e.g., Stock 1101, 2330).  
* We have an LLM.  
* **PROBLEM:** If we ask the LLM, "Should I buy stock 1101?", what happens?  
* **ANSWER:** The LLM knows nothing about stock 1101's data from *our private fin\_data\_smallset.csv file*.  
* Its training data is old (e.g., from 2023\) and generic. It cannot see our files.

## **Slide 7: The Solution: RAG**

* **RAG \= Retrieval-Augmented Generation**  
* It's the most important concept for using LLMs with private data.  
* **The Idea:** Don't *ask* the LLM a question it can't answer. *Give* it the data it needs *inside the prompt* and ask it to summarize.

**Analogy:**

* **Bad Prompt (No RAG):** "Hey, what's on page 5 of the book in my backpack?" (LLM: "I can't see your backpack.")  
* **Good Prompt (RAG):** "Here is the text from page 5: \[...text...\]. Please summarize it for me." (LLM: "Certainly\!")

## **Slide 8: RAG Explained Visually**

1. **User Query:** "Analyze stock 1101"  
2. **Our Code (Retrieval):**  
   * *Retrieves* all historical data for '1101' from fin\_data\_smallset.csv.  
3. **Our Code (Augmentation):**  
   * *Creates a summary* of that data (e.g., "EPS Trend: 1.2, 1.5, 1.3...").  
   * *Augments (inserts)* this summary into the prompt.  
4. **LLM (Generation):**  
   * Receives the full prompt: "Analyze stock 1101\. Here is its data: \[Data Summary...\]"  
   * *Generates* the analysis based *only* on the data we provided.

## **Slide 9: Step 2: RAG in Practice**

* **Retrieval:** For each stock in selected\_stocks.csv, we re-load the *full* fin\_data\_smallset.csv and filter it.

\# For loop: for stock in selected\_stocks...  
stock\_history\_df \= full\_fin\_df\[full\_fin\_df\['公司'\] \== stock\_code\]

* **Augmentation:** We create a simple text summary of its trends.

eps\_data \= stock\_history\_df\['每股盈餘'\].tail(8) \# Get last 8 quarters  
eps\_trend \= ", ".join(eps\_data.astype(str))  
history\_summary \= f"- Recent EPS Trend: {eps\_trend}"

## **Slide 10: Step 3: Prompt Engineering**

* Now we build our "Good Prompt" using RAG.  
* A good prompt has three parts:  
  1. **System Prompt (The Role):** "Who you are."  
  2. **Context (The Data):** "What you know." (This is our RAG summary)  
  3. **User Query (The Task):** "What to do."

## **Slide 11: Our Prompt Structure**

**1\. System Prompt:**

"You are a professional financial analyst for Taiwanese stocks. Be objective, professional, and use Traditional Chinese."

**2\. Context (Data from RAG):**

"Here is the historical financial summary for {Stock Name}:

* Recent EPS Trend: 1.7, 3.0, 3.5, 3.1  
* Recent Op. Margin Trend: 5%, 7%, 8%, 6%  
* Recent Current Ratio Trend: 1.8, 1.9, 1.8, 2.0"

**3\. User Query (Task):**

"Based *only* on this data, please analyze this company's:

1. Main Strengths (Pros)  
2. Potential Risks (Cons)  
3. A final rating (e.g., Buy, Hold, Sell) and your reasoning."

## **Slide 12: Step 4: Putting It All Together**

* Our llm\_analyzer.py script becomes a simple loop:  
  1. Read selected\_stocks.csv.  
  2. for each stock in the list:  
  3. **Retrieve** its history from fin\_data\_smallset.csv.  
  4. **Augment** a prompt with a summary of that history.  
  5. **Generate** an analysis by sending the prompt to the Ollama API.  
  6. Print the LLM's response.  
  7. Repeat.

## **Slide 13: Interpreting the Output (The Final Step)**

* The LLM gives us a beautifully written report. Now what?  
* **Pros of the LLM Output:**  
  * Finds trends we might miss (e.g., "I see EPS is rising but margin is shrinking").  
  * Excellent at summarizing data into human-readable text.  
  * Provides a "second opinion."  
* **Cons (DANGERS):**  
  * **Hallucination:** It might "invent" reasons or data we didn't provide. (e.g., "This is due to their new factory...") \-\> We must verify\!  
  * **Overconfidence:** It will *sound* 100% correct, even when it's just guessing.  
  * **Garbage In, Garbage Out:** If our data summary (RAG) is bad, the analysis will be bad.

## **Slide 14: Course Conclusion**

* **Quant (Python)** is your *filter*. It's fast, cheap, and objective.  
* **Qual (LLM)** is your *analyst*. It's slow, expensive (time/compute), and subjective.  
* **NEVER** blindly trust the Quant screen.  
* **NEVER** blindly trust the LLM's analysis.  
* The human (YOU\!) is the final decision-maker, using Python to filter noise and LLMs to suggest insights.  
* **This workflow (Quant \-\> Qual) is the future of financial analysis.**