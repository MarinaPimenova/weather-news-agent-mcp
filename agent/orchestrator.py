import re
from agent.tools import get_weather_tool, get_news_tool


class AgentOrchestrator:

    async def handle_query(self, query: str):
        query_lower = query.lower()

        results = {}

        if "weather" in query_lower:
            city = self.extract_city(query_lower)
            results["weather"] = await get_weather_tool(city)

        if "news" in query_lower:
            topic = self.extract_topic(query_lower)
            results["news"] = await get_news_tool(topic)

        return results

    def extract_city(self, query: str):
        # naive extraction
        words = query.split()
        for word in words:
            if word in ["vilnius", "berlin", "paris"]:
                return word
        return "vilnius"

    def extract_topic(self, query: str):
        match = re.search(r"news about (.+)", query)
        return match.group(1) if match else "technology"