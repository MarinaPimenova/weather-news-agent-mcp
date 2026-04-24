# Weather & News Agent App (MCP + LLM + Streamlit)

## 📌 Overview

This project is a **true intelligent agent** that uses:

* **LangChain** for LLM-powered agent orchestration
* **Streamlit** for UI
* **MCP (Model Context Protocol)** clients for external data:
    * Weather: Open-Meteo (no API key)
    * News: Google News RSS (no API key)
    * Geocoding: Nominatim (no API key)

The agent uses **natural language understanding** and **chain-of-thought reasoning** to:
- 🌦️ Get weather for ANY city (not hardcoded)
- 📰 Find news about any topic
- 🔄 Handle complex multi-tool queries intelligently

### Example Queries:
- "What's the weather in Paris?"
- "Tell me about AI news"
- "Weather in Berlin and news about Germany"
- "Latest technology updates in Tokyo"

---

## 🏗️ Architecture Evolution

### Before (Rule-based Router)
```
User Query → If/Else Router → Hardcoded Tools
```

### After (LLM-powered Agent)
```
User Query → LLM (Reasoning) → Agents Toolkit → MCP Clients
                ↓
        (understands intent, plans tools, reasons about results)
```

---

## How It Works

1. **User Query**: "What's the weather in Paris and latest AI news?"
2. **LLM Understanding**: Agent parses intent (2 tools needed)
3. **Tool Selection**: Decides to call `get_weather` + `get_news`
4. **Execution**:
    - `get_weather("Paris")` → Geocoding MCP → Weather MCP
    - `get_news("AI")` → News MCP
5. **Result Composition**: LLM formats response naturally

---

## ⚙️ Tech Stack

* **Python 3.11+**
* **LangChain** - Orchestration & LLM framework
* **Streamlit** - UI
* **MCP (Model Context Protocol)** - Structured APIs
* **HTTPX** - Async HTTP client
* **Geopy** - Geocoding
* **Pydantic** - Data validation
* **OpenAI** or **Anthropic** - LLM providers

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install --user -r requirements.txt

pip install -r requirements.txt --force-reinstall
```

```bash
pip uninstall langchain -y
pip install -r requirements.txt
pip install --upgrade langchain langchain-core langchain-community langchain-openai
```

### 2. Set Up LLM Provider

#### Using OpenAI (GPT-4 Recommended)
```bash
# Create .env file
cat > .env << EOF
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-your-key-here
OPENAI_MODEL=gpt-4-turbo
EOF
```

**Get key**: https://platform.openai.com/api-keys

### 3. Run the App
```bash
source .venv/Scripts/activate
streamlit run app.py
```

Open browser to: **http://localhost:8501/**



---

## 📁 Project Structure
├── app.py                      # Streamlit UI
├── config.py                   # Configuration & env vars
├── requirements.txt            # Python dependencies
├── .env.example               # Example environment config
│
├--─agent/
│   ├── orchestrator.py        # LLM-powered agent (TRUE AGENT)
│   ├── tools.py               # Tool definitions (dynamic cities)
│   ├── llm_factory.py         # LLM instance factory
│
├── mcp/
│   ├── weather_client.py      # Open-Meteo MCP client
│   ├── news_client.py         # Google News MCP client
│   ├── geocoding_client.py    # Nominatim geocoding MCP client (NEW)
│
├── services/
│   ├── weather_service.py     # Weather service layer
│   ├── news_service.py        # News service layer
│
├── models/
│   └── schemas.py             # Pydantic models
│
└── README.md                  # This file
```

---

## 🎯 Key Improvements Over Original

| Aspect | Before | After |
|--------|--------|-------|
| **Tool Routing** | Hardcoded if/else rules | LLM decides dynamically |
| **City Support** | 3 hardcoded cities (Vilnius, Berlin, Paris) | ANY city via Geocoding MCP |
| **Multi-tool Queries** | Not supported | Fully supported |
| **Agent Type** | Simple router | True ReAct agent with reasoning |
| **LLM Integration** | None | OpenAI/Anthropic support |
| **Extensibility** | Hard to add tools | Easy - just add Tool definition |

---

## 🧩 LangChain Agent Concepts

### ReAct (Reasoning + Acting)
The agent uses chain-of-thought reasoning:

```
Thought: I need to get weather in Paris
Action: get_weather with city="Paris"
Observation: [weather data]
Thought: Now I should get news about AI
Action: get_news with topic="AI"
Observation: [news data]
Final Answer: [Composed response]
```

---

## 🔧 Configuration

Edit `.env` file to control:

```env
# LLM Provider (openai or anthropic)
LLM_PROVIDER=openai

# OpenAI Settings
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4-turbo

# Anthropic Settings  
ANTHROPIC_API_KEY=sk-ant-...
ANTHROPIC_MODEL=claude-3-sonnet-20240229

# Agent Verbosity
AGENT_VERBOSE=true
```

---

## 💡 Learning Goals

✅ Understand LLM-powered agent orchestration
✅ Learn MCP (Model Context Protocol) implementation
✅ Build production-like Python applications
✅ Work with multiple LLM providers
✅ Implement ReAct reasoning pattern

---

## 📚 Resources

- [LangChain Agents](https://python.langchain.com/docs/modules/agents/)
- [MCP Protocol](https://modelcontextprotocol.io/)
- [OpenAI API](https://platform.openai.com/docs/api-reference)
- [Anthropic API](https://docs.anthropic.com/)
- [Streamlit Docs](https://docs.streamlit.io/)

---

## ⚠️ Notes

* Open-Meteo weather API requires no authentication
* Google News RSS feed used (no API key needed)
* Nominatim geocoding requires valid user agent
* LLM API calls **do incur costs** (OpenAI/Anthropic)
* This is a learning-focused implementation with room for production enhancements

---
