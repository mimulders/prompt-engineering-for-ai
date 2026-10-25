import getpass
import os

# Set up your LiteLLM client
if not os.getenv("ANTHROPIC_AUTH_TOKEN"):
    secret_key = getpass.getpass("Enter your LiteLLM API key: ")  # uses getpass to do this securely
    os.environ["ANTHROPIC_AUTH_TOKEN"] = secret_key
    
from langchain_litellm import ChatLiteLLM
from langchain_core.prompts.chat import ChatPromptTemplate

chat = ChatLiteLLM(
    model="claude-opus-4-5",   # Pick an Anthropic model name
    # provider="anthropic"
)

chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that generates company names"),
    ("human", "{text}")
])

result = chat_prompt_template.invoke({
    "text": "What would be a good company name for a company that makes colorful socks?"
})

ai_llm_result = chat.invoke(result)
print (type(result))
print(ai_llm_result.content)