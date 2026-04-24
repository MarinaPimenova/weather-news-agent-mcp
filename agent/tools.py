"""
Tool definitions for the LLM-based agent.
These tools are exposed to the LangChain agent for dynamic invocation.
"""

from services.weather_service import WeatherService
from services.news_service import NewsService
from mcp.geocoding_client import GeocodingMCPClient

weather_service = WeatherService()
news_service = NewsService()
geocoding_client = GeocodingMCPClient()


async def get_weather_tool(city: str):
    """
    Get current weather for any city in the world.

    Args:
        city: City name (e.g., "Paris", "Tokyo", "New York")

    Returns:
        Dictionary with current weather data
    """
    try:
        # Dynamic geocoding - supports ANY city, not hardcoded list
        lat, lon = await geocoding_client.get_coordinates(city)
        weather_data = await weather_service.get_weather_by_coords(lat, lon)
        return {
            "city": city,
            "coordinates": {"latitude": lat, "longitude": lon},
            "weather": weather_data,
            "status": "success"
        }
    except ValueError as e:
        return {"error": f"City not found: {city}", "status": "error"}
    except Exception as e:
        return {"error": f"Failed to fetch weather: {str(e)}", "status": "error"}


async def get_news_tool(topic: str):
    """
    Get latest news about a topic.

    Args:
        topic: Topic to search for (e.g., "AI", "Tesla", "climate change")

    Returns:
        List of news articles
    """
    try:
        news_data = await news_service.get_news(topic)
        return {
            "topic": topic,
            "articles": news_data,
            "status": "success"
        }
    except Exception as e:
        return {"error": f"Failed to fetch news: {str(e)}", "status": "error"}