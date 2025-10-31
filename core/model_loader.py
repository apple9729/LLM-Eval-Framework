from models.openai_client import OpenAIClient
from models.huggingface_client import HFClient
from models.local_model import LocalModel

def load_model(name):
    if name.startswith("hf:"):
        return HFClient(name.replace("hf:", ""))
    if name.startswith("openai:") or name.lower().startswith("gpt") or "openai" in name.lower():
        key = name.replace("openai:", "")
        return OpenAIClient(key or None)
    return LocalModel(name)
