"""Factory for creating LLM instances based on configuration"""

from config import LLM_PROVIDER, OPENAI_API_KEY, ANTHROPIC_API_KEY, DEFAULT_MODEL
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

def create_llm():
    """
    Factory function to create LLM instance based on environment configuration.

    Supports:
    - OpenAI (GPT-4, GPT-3.5-turbo)
    - Anthropic (Claude 3 family)

    Returns:
        ChatOpenAI or ChatAnthropic instance

    Raises:
        ValueError: If LLM provider not configured properly
    """

    if LLM_PROVIDER == "openai":
        if not OPENAI_API_KEY:
            raise ValueError(
                "OpenAI API key not found. "
                "Set OPENAI_API_KEY environment variable."
            )
        return ChatOpenAI(
            model=DEFAULT_MODEL,
            api_key=OPENAI_API_KEY,
            temperature=0.3  # Lower temperature for deterministic responses
        )

    elif LLM_PROVIDER == "anthropic":
        if not ANTHROPIC_API_KEY:
            raise ValueError(
                "Anthropic API key not found. "
                "Set ANTHROPIC_API_KEY environment variable."
            )
        return ChatAnthropic(
            model=DEFAULT_MODEL,
            api_key=ANTHROPIC_API_KEY,
            temperature=0.3
        )

    else:
        raise ValueError(
            f"Unknown LLM provider: {LLM_PROVIDER}. "
            "Use 'openai' or 'anthropic'."
        )
