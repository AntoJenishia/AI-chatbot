from groq import Groq
from config import load_api_key

def chatbot(messages, system_prompt="You are a helpful assistant specialized in Wi-Fi and network issues. Only answer questions that are directly related to Wi-Fi, internet connectivity, routers, modems, network troubleshooting, or similar topics. If a user asks about anything outside of Wi-Fi or networking, politely respond: \"I'm only able to assist with Wi-Fi and network-related questions.\""):
    """Process the user message and return the chatbot's response."""
    
    apikey= load_api_key()
    Client = Groq(api_key=apikey)
    
    if system_prompt:
        messages.insert(0, {"role": "system", "content": system_prompt})
       
    completion= Client.chat.completions.create(
          model="llama3-8b-8192",
          messages=messages,
          temperature=0.7)
    
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
          temperature=0.7)
    return completion.choices[0].message.content