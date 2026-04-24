from mcp.base_client import MCPClient
import httpx


class GeocodingMCPClient(MCPClient):
    BASE_URL = "https://geocoding-api.open-meteo.com/v1/search"

    async def execute(self, city: str):
        params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(self.BASE_URL, params=params)
            response.raise_for_status()
            return response.json()

    async def get_coordinates(self, city: str):
        data = await self.execute(city)

        if not data.get("results"):
            raise ValueError(f"City '{city}' not found")

        result = data["results"][0]
        return result["latitude"], result["longitude"]