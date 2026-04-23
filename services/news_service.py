"""
News Service - Bridges application logic to News MCP client.
The MCP client (NewsMCPClient) encapsulates all HTTP communication.
"""

from mcp.news_client import NewsMCPClient

class NewsService:

    def __init__(self):
        self.client = NewsMCPClient()

    async def get_news(self, topic: str):
        try:
            data = await self.client.get_news(topic)
            return data  # ✅ already a list
        except Exception as e:
            return [{"title": f"Error fetching news: {str(e)}"}]