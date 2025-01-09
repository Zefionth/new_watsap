from openai_api import get_names
from kinopoisk_api import get_info_movies
from shikimoriapi import get_info_anime

def fetch_info(name: str, category: str):
    """Получает информацию на основе категории."""
    if category == 'movies':
        return get_info_movies(name)
    return get_info_anime(name)

def get_recommendations(query: str, category: str) -> list:
    """Получает рекомендации на основе запроса и категории."""
    recommendations = []
    names = get_names(query, category).values()

    for name in names:
        if name is not None:
            info = fetch_info(name, category)
            recommendations.append(info)

    return recommendations