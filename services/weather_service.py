from mcp.weather_client import WeatherMCPClient

class WeatherService:

    def __init__(self):
        self.client = WeatherMCPClient()

    async def get_weather_by_coords(self, lat, lon):
        data = await self.client.get_weather(lat, lon)
        return data["current_weather"]