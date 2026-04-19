# Weather & News Agent App (MCP + Streamlit)

## 📌 Overview

This project is a Python-based application that uses:

* **Streamlit** for UI
* **Agent orchestration** for handling user queries
* **MCP (Model Context Protocol) servers** for external data:

    * Weather: Open-Meteo (no API key)
    * News: GNews (no API key via MCP wrapper)

The app answers questions like:

* "What is the weather in Vilnius?"
* "Latest news about AI"
* "Weather in Paris and news about France"

---

## 🧠 Architecture

User → Streamlit UI → Agent → Tools (MCP Clients)
├── Weather MCP (Open-Meteo)
└── News MCP (GNews)

---

## ⚙️ Tech Stack

* Python 3.11+
* Streamlit
* MCP (Model Context Protocol)
* HTTPX (for API calls)
* Pydantic (data validation)
* Asyncio

---

## 🚀 Features

* Natural language query handling
* Tool-based agent execution
* Modular MCP client design
* No API keys required

---

## 📁 Project Structure

```
weather-news-agent-mcp/
│
├── app.py                  # Streamlit UI
├── agent/
│   ├── orchestrator.py     # Agent logic
│   ├── tools.py            # Tool definitions
│
├── mcp/
│   ├── weather_client.py   # Open-Meteo MCP client
│   ├── news_client.py      # GNews MCP client
│
├── models/
│   ├── schemas.py          # Pydantic models
│
├── services/
│   ├── weather_service.py
│   ├── news_service.py
│
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```
or
```bash
source .venv/Scripts/activate
streamlit run app.py
```

It's available on http://localhost:8501/

---

## 💡 Example Queries

* "Weather in Berlin"
* "Latest news about Tesla"
* "Weather in Tokyo and news about Japan"

---

## 🧩 Key Concepts

### Agent

Decides:

* What user wants
* Which tool(s) to call

### MCP Client

Acts as:

* Structured interface to external APIs

### Tools

Functions exposed to the agent:

* `get_weather(city)`
* `get_news(topic)`

---

## 📚 Learning Goals

* Understand Agent orchestration
* Use MCP for structured API integration
* Build production-like Python apps

---

## ⚠️ Notes

* Open-Meteo does not require API key
* GNews free endpoint is used via MCP wrapper
* This is a learning-focused implementation

---
🧩 Architecture Explanation (Java mindset)

Think of this like a Spring Boot app:

| Java Concept    | Python Equivalent       |
| --------------- | ----------------------- |
| Controller      | `app.py` (Streamlit)    |
| Service         | `services/`             |
| DTO             | `models/schemas.py`     |
| External Client | `mcp/*_client.py`       |
| Business Logic  | `agent/orchestrator.py` |

Java analogy

Think of it like:
| Java world            | Python world           |
| --------------------- | ---------------------- |
| `mvn spring-boot:run` | `streamlit run app.py` |
| `.m2 dependencies`    | `.venv packages`       |
| classpath             | activated venv         |
