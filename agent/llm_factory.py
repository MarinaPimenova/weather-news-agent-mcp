import os
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic


def create_llm():
    provider = os.getenv("LLM_PROVIDER", "openai")
    model = os.getenv("LLM_MODEL", "gpt-3.5-turbo")

    if provider == "openai":
        api_key = os.getenv("LLM_API_KEY")
        if not api_key:
            raise ValueError("LLM_API_KEY not set")

        return ChatOpenAI(
            model=model,
            api_key=api_key,
            temperature=0.3
        )

    elif provider == "anthropic":
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not set")

        return ChatAnthropic(
            model=model,
            api_key=api_key,
            temperature=0.3
        )

    else:
        raise ValueError(f"Unknown provider: {provider}")