from langchain_groq import ChatGroq
from src.config.settings import setting


def get_groq_llm():
    return ChatGroq(
        api_key=setting.GROQ_API_KEY,
        model=setting.MODEL_NAME,
        temperature=setting.TEMPERATURE
    )

