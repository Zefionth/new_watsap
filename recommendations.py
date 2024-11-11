from openai_api import get_names
from kinopoisk_api import get_info_movies

def get_recommendations(query, category):

    recommendations = []

    names = get_names(query, category).values()
    if names:
        if category == 'movies':
            for name in names:
                info = get_info_movies(name)
                recommendations.append(info)

    return recommendations