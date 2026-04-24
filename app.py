import streamlit as st
import asyncio
from dotenv import load_dotenv
from agent.orchestrator import AgentOrchestrator

load_dotenv()

st.title("Weather News Agent")

query = st.text_input("Ask something:")

if "agent" not in st.session_state:
    st.session_state.agent = AgentOrchestrator()

if st.button("Run Agent") and query:

    async def run():
        return await st.session_state.agent.handle_query(query)

    result = asyncio.run(run())

    st.write("### Response")
    st.json(result)