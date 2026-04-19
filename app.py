import streamlit as st
import asyncio
from agent.orchestrator import AgentOrchestrator

st.title("🌦️ Weather & News Agent")

query = st.text_input("Ask something:")

if query:
    orchestrator = AgentOrchestrator()

    result = asyncio.run(orchestrator.handle_query(query))

    if "weather" in result:
        st.subheader("Weather")
        st.json(result["weather"])

    if "news" in result:
        st.subheader("News")
        for article in result["news"]:
            st.write(article["title"])