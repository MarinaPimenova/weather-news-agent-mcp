"""
Geocoding MCP Client - Converts city names to coordinates
This MCP abstracts the conversion from natural language city names to latitude/longitude.
Currently uses Open-Meteo's Geocoding API (free, no key required).
"""

import httpx


class GeocodingMCPClient:
    """
    MCP Client for geocoding services.
    Provides structured interface to convert city names to coordinates.
    HTTP calls are encapsulated within this MCP layer.
    """
    BASE_URL = "https://geocoding-api.open-meteo.com/v1/search"

    async def get_coordinates(self, city: str) -> tuple:
        """
        Get latitude and longitude for a city name.

        Args:
            city: City name (e.g., "Paris", "New York", "Tokyo")

        Returns:
            Tuple of (latitude, longitude)

        Raises:
            ValueError: If city not found
            Exception: If API call fails
        """
        params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(self.BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()

            if not data.get("results"):
                raise ValueError(f"City '{city}' not found")

            result = data["results"][0]
            lat = result["latitude"]
            lon = result["longitude"]

            return (lat, lon)