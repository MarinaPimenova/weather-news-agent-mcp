import re

from services.weather_service import WeatherService
from services.news_service import NewsService
from mcp.geocoding_client import GeocodingMCPClient

weather_service = WeatherService()
news_service = NewsService()
geocoding_client = GeocodingMCPClient()

def normalize_llm_input(text: str) -> str:
    """
    Extract the most likely entity (city/topic) from LLM output.
    Works for both weather and news tools.
    """

    if not text:
        return ""

    text = text.lower().strip()

    # remove common question patterns
    text = re.sub(r"what('s| is)?", "", text)
    text = re.sub(r"weather in", "", text)
    text = re.sub(r"news about", "", text)
    text = re.sub(r"get", "", text)

    # remove punctuation
    text = re.sub(r"[?.,!]", " ", text)

    # split multi-intent queries
    parts = re.split(r"\band\b", text)

    candidate = parts[0].strip()

    # remove extra filler words
    words = candidate.split()

    # keep last meaningful tokens (cities/topics are usually short)
    candidate = " ".join(words[-3:])

    return candidate.strip().title()

async def get_weather_tool(city: str):
    """
    MCP Weather Tool (pure execution layer)
    """

    try:
        clean_city = normalize_llm_input(city)

        if not clean_city:
            return {
                "error": "Empty city input",
                "status": "error"
            }

        lat, lon = await geocoding_client.get_coordinates(clean_city)

        weather_data = await weather_service.get_weather_by_coords(lat, lon)

        return {
            "city": clean_city,
            "coordinates": {
                "latitude": lat,
                "longitude": lon
            },
            "weather": weather_data,
            "status": "success"
        }

    except ValueError:
        return {
            "error": f"City not found: {city}",
            "status": "error"
        }

    except Exception as e:
        return {
            "error": f"Weather tool failed: {str(e)}",
            "status": "error"
        }

async def get_news_tool(topic: str):
    """
    MCP News Tool (pure execution layer)
    """

    try:
        clean_topic = normalize_llm_input(topic)

        if not clean_topic:
            return {
                "error": "Empty topic input",
                "status": "error"
            }

        news_data = await news_service.get_news(clean_topic)

        return {
            "topic": clean_topic,
            "articles": news_data,
            "status": "success"
        }

    except Exception as e:
        return {
            "error": f"News tool failed: {str(e)}",
            "status": "error"
        }