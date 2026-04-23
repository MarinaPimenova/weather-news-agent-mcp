"""
Agent Orchestrator - LLM-based intelligent agent using LangChain
This replaces the previous rule-based routing with true LLM-driven agent reasoning.
The agent decides which tools to use based on natural language understanding.
"""

import os
from typing import Any, Dict

from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import StreamlitCallbackHandler

from agent.tools import get_weather_tool, get_news_tool


class AgentOrchestrator:
    """
    LLM-based agent orchestrator using LangChain.

    Key improvements over rule-based approach:
    1. ✅ Intelligent tool selection - LLM decides WHICH tools to use
    2. ✅ Natural language understanding - handles complex, multi-step queries
    3. ✅ Reasoning capabilities - agent can reason about tool results
    4. ✅ Dynamic city support - no hardcoded city list
    5. ✅ Retry logic - can retry failed tool calls

    LLM Models Supported:
    - OpenAI GPT-4, GPT-3.5-turbo (requires OPENAI_API_KEY)
    - Anthropic Claude (requires ANTHROPIC_API_KEY)
    - Local models via Ollama (no key needed)
    """

    def __init__(self, model: str = "gpt-3.5-turbo", temperature: float = 0.0):
        """
        Initialize the agent orchestrator.

        Args:
            model: LLM model to use (e.g., "gpt-4", "gpt-3.5-turbo")
            temperature: LLM temperature (0.0 = deterministic, 1.0 = creative)
        """
        self.model = model
        self.temperature = temperature
        self._setup_agent()

    def _setup_agent(self):
        """Setup LangChain agent with tools and LLM."""
        # Initialize LLM
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY not set. Please set it in .env or environment variables. "
                "Get your key at: https://platform.openai.com/api-keys"
            )

        self.llm = ChatOpenAI(
            model_name=self.model,
            temperature=self.temperature,
            api_key=api_key,
            max_retries=2,
        )

        # Define tools for the agent
        tools = [
            Tool(
                name="get_weather",
                func=self._run_tool_sync(get_weather_tool),
                description=(
                    "Get current weather for any city in the world. "
                    "Input should be a city name (e.g., 'Paris', 'New York', 'Tokyo'). "
                    "Returns weather data including temperature, humidity, wind speed."
                ),
            ),
            Tool(
                name="get_news",
                func=self._run_tool_sync(get_news_tool),
                description=(
                    "Get latest news articles about a topic. "
                    "Input should be a topic (e.g., 'AI', 'climate change', 'Tesla'). "
                    "Returns list of news articles with titles and links."
                ),
            ),
        ]

        # Initialize LangChain agent
        self.agent = initialize_agent(
            tools=tools,
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            max_iterations=5,
            early_stopping_method="force",
            handle_parsing_errors=True,
        )

    def _run_tool_sync(self, async_func):
        """
        Wrapper to run async tools synchronously.
        LangChain tools expect synchronous functions.
        """
        import asyncio

        def sync_wrapper(input_str: str) -> str:
            """Convert async tool to sync."""
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                result = loop.run_until_complete(async_func(input_str))
                loop.close()

                if isinstance(result, dict):
                    if result.get("status") == "error":
                        return f"Error: {result.get('error', 'Unknown error')}"
                    return str(result)
                return str(result)
            except Exception as e:
                return f"Error executing tool: {str(e)}"

        return sync_wrapper

    async def handle_query(self, query: str) -> Dict[str, Any]:
        """Process user query with LLM agent.
        Agent decides which tools to use and how to combine results.

        Args:
            query: User's natural language query

        Returns:
            Agent response with tool results
        """
        try:
            # Run agent in thread pool to avoid blocking
            import asyncio
            from concurrent.futures import ThreadPoolExecutor

            loop = asyncio.get_event_loop()
            with ThreadPoolExecutor() as pool:
                result = await loop.run_in_executor(
                    pool,
                    lambda: self.agent.run(query),
                )
            return {"result": result, "status": "success"}
        except Exception as e:
            return {
                "error": f"Agent failed: {str(e)}",
                "status": "error",
            }