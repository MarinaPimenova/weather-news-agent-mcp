import streamlit as st
import asyncio

class AsyncAgent:
    async def run(self):
        # Replace this with your LLM integration logic
        await asyncio.sleep(1)  # Simulating async work
        return "Data from LLM"

async def main():
    agent = AsyncAgent()
    result = await agent.run()
    st.write(result)

if __name__ == '__main__':
    st.title('Weather News Agent')
    st.button('Run Agent', on_click=lambda: asyncio.run(main()))