# **Lesson 2: Qualitative Analysis with LLMs**

## **Slide 5: Step 1: Connecting to Ollama**

* We use the requests library in Python.  
* We send an HTTP POST request to the Ollama API (/api/generate).  
* The payload is a JSON object containing our model and prompt.

```python
import requests

payload = {  
    "model": "llama3", # Or whatever model you have  
    "prompt": "Why is the sky blue?",  
    "stream": False  
}

response = requests.post(  
    "http://localhost:11434/api/generate",   
    json=payload  
)

print(response.json()['response'])
```
