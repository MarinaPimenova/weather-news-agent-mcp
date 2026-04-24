from mcp.base_client import MCPClient
import httpx


class WeatherMCPClient(MCPClient):
    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    async def execute(self, latitude: float, longitude: float):
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(self.BASE_URL, params=params)
            response.raise_for_status()
            return response.json()

    async def get_weather(self, latitude: float, longitude: float):
        data = await self.execute(latitude, longitude)
        return data