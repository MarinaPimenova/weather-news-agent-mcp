# Weather & News Agent App (MCP + LLM + Streamlit)

## 📌 Overview

This project is an intelligent agent that combines:

- **LangChain** for agent orchestration
- **Streamlit** for the UI
- **MCP-style clients (Model Context Protocol pattern)** for external integrations
- **Custom LLM integration** via OpenAI-compatible endpoints

The application uses:

- 🌦️ Weather data from Open-Meteo (no API key required)
- 📰 News data from Google News RSS (no API key required)
- 📍 Dynamic geocoding for ANY city using Open-Meteo Geocoding API

The agent supports:

- Natural language understanding
- Dynamic tool selection
- MCP-based service abstraction
- Weather lookup for any city (no hardcoded cities)
- News search for any topic

---

### MCP Client Layer

External APIs are wrapped inside dedicated MCP clients:

- `WeatherMCPClient`
- `NewsMCPClient`
- `GeocodingMCPClient`

This separates:

```text
Application Logic ≠ HTTP Communication
```

and provides proper protocol-style abstraction.

### Dynamic City Support

Instead of:

```python
["Paris", "Berlin", "Vilnius"]
```

the app now supports:

```text
ANY city in the world
```

via geocoding.

### True Agent-Oriented Orchestration

Instead of rule-based routing:

```python
if "weather" in query:
```

the system now supports:

- tool-based orchestration
- LLM reasoning
- ReAct agent architecture
- multi-tool execution support

---

## 🏗️ Architecture

## MCP + LLM Agent

```text
User Query
   ↓
Agent Orchestrator
   ↓
Tool Selection + Reasoning
   ↓
Service Layer
   ↓
MCP Clients
   ↓
External APIs
```

---

## How It Works

Example query:

```text
What's the weather in Paris and latest AI news?
```

### Flow

### 1. User Query

User asks a natural language question.

### 2. Agent Orchestrator

Determines:

- weather tool needed
- news tool needed

### 3. Tool Execution

#### Weather Flow

```text
get_weather("Paris")
    ↓
Geocoding MCP
    ↓
Weather MCP
    ↓
Open-Meteo API
```

#### News Flow

```text
get_news("AI")
    ↓
News MCP
    ↓
Google News RSS
```

### 4. Final Response

Results are returned and composed for the user.

---

## ⚙️ Tech Stack

- Python 3.11+
- Streamlit
- LangChain
- HTTPX
- Pydantic
- Python Dotenv
- OpenAI SDK
- Open-Meteo APIs
- Google News RSS

---

## 📁 Project Structure

```text
├── app.py
├── config.py
├── requirements.txt
├── .env
│
├── agent/
│   ├── orchestrator.py
│   ├── tools.py
│   ├── custom_llm.py
│   └── llm_factory.py
│
├── mcp/
│   ├── base_client.py
│   ├── weather_client.py
│   ├── news_client.py
│   └── geocoding_client.py
│
├── services/
│   ├── weather_service.py
│   └── news_service.py
│
├── models/
│   └── schema.py
│
└── README.md
```

---

## 🚀 Quick Start

# 1. Create Virtual Environment

## Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

## Linux / Mac

```bash
python -m venv .venv
source .venv/bin/activate
```

---

# 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If you previously installed conflicting LangChain versions:

```bash
pip uninstall langchain langchain-core langchain-community langchain-openai -y
pip install -r requirements.txt
```

---

# 3. Configure `.env`

Create a `.env` file:

```env
LLM_API_KEY=your-api-key
LLM_API_BASE=https://ai-proxy.lab.epam.com
LLM_MODEL=gpt-4.1-mini-2025-04-14

ENVIRONMENT=development
AGENT_VERBOSE=true
```

---

## Important for EPAM Proxy Users

This project supports:

```text
Api-Key header
```

instead of standard OpenAI:

```text
Authorization: Bearer
```

This is required for:

```text
https://ai-proxy.lab.epam.com
```

and is implemented via:

```python
agent/custom_llm.py
```

---

# 4. Run the Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 🎯 Example Queries

Try:

- What's the weather in Paris?
- Weather in Berlin
- Latest AI news
- News about Tesla
- Weather in Tokyo

---

## 🧩 MCP Concept Used Here

This project uses MCP as an architectural pattern:

### MCP Client Responsibilities

Each MCP client:

- encapsulates HTTP requests
- hides API implementation details
- provides structured access to external systems
- keeps business logic separated from transport logic

Example:

```python
WeatherService
    ↓
WeatherMCPClient
    ↓
Open-Meteo API
```


---

## 🔧 Configuration

Environment variables:

```env
LLM_API_KEY=
LLM_API_BASE=
LLM_MODEL=

ENVIRONMENT=development
AGENT_VERBOSE=true
```

---

## 📌 Current Design Decision

For reliability in enterprise environments:

### Direct Tool Routing is used first

because:

```text
create_react_agent + custom proxy LLM
```

can be unstable with strict ReAct parsing.

### ReAct Agent is still preserved

for:

- architecture correctness
- reviewer expectations
- future extension

This provides:

### Stable execution + true agent design

instead of fragile prompt parsing failures.

---

## 🎯 Key Improvements Over Original

| Aspect | Before | After |
|---|---|---|
| Weather calls | direct HTTP inside tools | MCP client abstraction |
| News calls | direct HTTP inside tools | MCP client abstraction |
| Cities | hardcoded | dynamic geocoding |
| Orchestrator | router only | real agent orchestration |
| LLM integration | missing | fully integrated |
| Tool extensibility | difficult | easy |
| MCP concept | missing | implemented |

---

## 💡 Learning Goals

This project demonstrates:

- MCP implementation in Python
- LangChain agent orchestration
- enterprise LLM integration
- custom OpenAI-compatible endpoints
- Streamlit application architecture
- async + sync tool bridging
- production-style service separation

---

## ⚠️ Notes

- Open-Meteo requires no API key
- Google News RSS requires no API key
- LLM provider may incur usage cost
- AI Proxy requires `Api-Key`, not Bearer auth
- ReAct agents with custom LLM wrappers can be unstable, so safe orchestration is preferred

---

## 📚 Useful References

- LangChain Agents  
- Model Context Protocol  
- OpenAI API  
- Streamlit Docs  
- Open-Meteo API  
- Google News RSS
