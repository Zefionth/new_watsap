from openai_api import get_names
from kinopoisk_api import get_info

def get_recommendations(query):

    recommendations = []

    names = get_names(query).values()
    if names:
        for name in names:
            info = get_info(name)
            recommendations.append(info)

    return recommendations