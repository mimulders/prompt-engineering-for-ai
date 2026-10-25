import os
print(
    os.getenv("ANTHROPIC_AUTH_TOKEN"),
    os.getenv("ANTHROPIC_BASE_URL"),
    os.getenv("ANTHROPIC_CUSTOM_HEADERS")
)
# output formatting
#TODO

# Using LiteLLM directly
import litellm
response = litellm.completion(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Hello, who are you?"}],
    # API_KEY and BASE_URL are read from environment variables
)
print(response)

# another way -- does not work yet
# via API call, via langchain + LiteLLM
from langchain_litellm import ChatLiteLLM

chat = ChatLiteLLM(
    model="claude-opus-4-5",
    # llm_provider="anthropic",               # mention the provider to use
    # # No need to pass API key/URL if using env vars
)

response = chat.invoke("Hello, who are you?")
print(response)