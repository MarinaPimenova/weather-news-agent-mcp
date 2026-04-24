from mcp.base_client import MCPClient
import httpx
import xml.etree.ElementTree as ET


class NewsMCPClient(MCPClient):
    BASE_URL = "https://news.google.com/rss/search"

    async def execute(self, query: str):
        params = {
            "q": query,
            "hl": "en-US",
            "gl": "US",
            "ceid": "US:en"
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(self.BASE_URL, params=params)
            response.raise_for_status()
            return response.text

    async def get_news(self, query: str):
        xml_data = await self.execute(query)
        return self.parse_rss(xml_data)

    def parse_rss(self, xml_data: str):
        root = ET.fromstring(xml_data)
        articles = []

        for item in root.findall(".//item")[:5]:
            articles.append({
                "title": item.find("title").text,
                "link": item.find("link").text
            })

        return articles