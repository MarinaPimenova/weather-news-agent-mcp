from services.weather_service import WeatherService
from services.news_service import NewsService

weather_service = WeatherService()
news_service = NewsService()


async def get_weather_tool(city: str):
    # Simplification: hardcoded coordinates
    city_coords = {
        "vilnius": (54.6872, 25.2797),
        "berlin": (52.52, 13.4050),
        "paris": (48.8566, 2.3522)
    }

    lat, lon = city_coords.get(city.lower(), (54.6872, 25.2797))
    return await weather_service.get_weather_by_coords(lat, lon)


async def get_news_tool(topic: str):
    return await news_service.get_news(topic)