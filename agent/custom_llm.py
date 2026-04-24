from typing import List, Optional, Any
import os
import httpx

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage, BaseMessage
from langchain_core.outputs import ChatGeneration, ChatResult


class EPAMChatModel(BaseChatModel):
    """
    Custom LangChain-compatible chat model
    using EPAM AI Proxy + Api-Key header.
    """

    model_name: str = "gpt-4.1-mini-2025-04-14"

    @property
    def _llm_type(self) -> str:
        return "epam_proxy_chat_model"

    def _generate(
            self,
            messages: List[BaseMessage],
            stop: Optional[List[str]] = None,
            run_manager=None,
            **kwargs: Any,
    ) -> ChatResult:

        api_key = os.getenv("LLM_API_KEY")
        base_url = os.getenv("LLM_API_BASE")
        model = os.getenv("LLM_MODEL", self.model_name)

        if not api_key:
            raise ValueError("LLM_API_KEY not set")

        if not base_url:
            raise ValueError("LLM_API_BASE not set")

        payload_messages = []

        for msg in messages:
            role = "user"

            msg_type = msg.__class__.__name__

            if msg_type == "SystemMessage":
                role = "system"
            elif msg_type == "HumanMessage":
                role = "user"
            elif msg_type == "AIMessage":
                role = "assistant"

            payload_messages.append({
                "role": role,
                "content": str(msg.content)
            })

        response = httpx.post(
            f"{base_url}/openai/deployments/{model}/chat/completions",
            headers={
                "Api-Key": api_key
            },
            json={
                "model": model,
                "messages": payload_messages
            },
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        content = data["choices"][0]["message"]["content"]

        return ChatResult(
            generations=[
                ChatGeneration(
                    message=AIMessage(content=content)
                )
            ]
        )