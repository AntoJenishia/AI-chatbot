from groq import Groq
from config import load_api_key

def chatbot(messages, system_prompt=None):
    """Process the user message and return the chatbot's response."""
    
    apikey= load_api_key()
    Client = Groq(api_key=apikey)
    
    if system_prompt:
        messages.insert(0, {"role": "system", "content": system_prompt})
       
    completion= Client.chat.completions.create(
          model="llama3-8b-8192",
          messages=messages,
          temperature=0)
    
    return completion.choices[0].message.content

def chatbot2(user_message: str, system_prompt: str=None):
    """Process the user message and return the chatbot's response via E-mail."""
    
    apikey= load_api_key()
    Client = Groq(api_key=apikey)
    messages=[]
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": user_message})
    
    completion= Client.chat.completions.create(
          model="llama3-8b-8192",
          messages=messages,
          temperature=0)
    return completion.choices[0].message.content