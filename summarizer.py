
from client import chatbot2

def summarize_chat(messages):
    """
    Summarize the entire chatbot history/conversation.
    :param messages: List of dicts with 'role' and 'content' keys
    :return: Summary string
    """
    # Combine all user and assistant messages into a single string
    conversation = "\n".join([
        f"{msg['role'].capitalize()}: {msg['content']}" for msg in messages
    ])
    # Use chatbot2 with a summarization prompt
    summary_prompt = (
        "Summarize the following chatbot conversation, focusing on the main topics, user queries, and important details. "
        "Make the summary concise and clear.\n\n" + conversation
    )
    return chatbot2(summary_prompt)
