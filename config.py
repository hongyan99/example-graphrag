import os
from dotenv import load_dotenv
from llm_adapter_factory import get_llm_adapter

load_dotenv()

# Define the provider and settings
LLM_ADAPTER = os.getenv("LLM_PROVIDER", "openai")
SETTINGS = {
    'openai': {
        'api_key': os.getenv("OPENAI_API_KEY"),
        'model': os.getenv("OPENAI_MODEL", "gpt-4o")
    },
    'ollama': {
        'base_url': os.getenv("OLLAMA_BASE_URL", "http://192.168.86.112:11434"),
        'model': os.getenv("OLLAMA_MODEL", "llama2")
    }
}

# Dynamically load the adapter
llm_adapter = get_llm_adapter(LLM_ADAPTER, SETTINGS[LLM_ADAPTER])
