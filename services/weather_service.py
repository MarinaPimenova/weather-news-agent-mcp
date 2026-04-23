"""
Weather Service - Bridges application logic to Weather MCP client.
The MCP client (WeatherMCPClient) encapsulates all HTTP communication.
"""

from mcp.weather_client import WeatherMCPClient


class WeatherService:
    """
    Service layer for weather operations.
    Delegates to MCP client for actual API communication.
    """

    def __init__(self):
        self.client = WeatherMCPClient()

    async def get_weather_by_coords(self, lat: float, lon: float):
        """
        Get weather for specific coordinates.

        Args:
            lat: Latitude
            lon: Longitude

        Returns:
            Current weather data from Open-Meteo API
        """

        data = await self.client.get_weather(lat, lon)
        return data["current_weather"]