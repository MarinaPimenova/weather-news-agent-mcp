# services/news_service.py

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