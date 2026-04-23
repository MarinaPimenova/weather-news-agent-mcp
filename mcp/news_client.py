import httpx
import xml.etree.ElementTree as ET


class NewsMCPClient:
    BASE_URL = "https://news.google.com/rss/search"

    async def get_news(self, query: str):
        params = {
            "q": query,
            "hl": "en-US",
            "gl": "US",
            "ceid": "US:en"
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(self.BASE_URL, params=params)
            response.raise_for_status()

            return self.parse_rss(response.text)

    def parse_rss(self, xml_data: str):
        """Parse RSS XML response into article list."""
        root = ET.fromstring(xml_data)
        articles = []

        for item in root.findall(".//item")[:5]:
            articles.append({
                "title": item.find("title").text,
                "link": item.find("link").text
            })

        return articles