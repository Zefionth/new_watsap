import requests
from config import KINOPOISK_API_TOKEN

def get_info(name: str) -> str:
    url = f"https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword={name}"
    headers = {
        'X-API-KEY': KINOPOISK_API_TOKEN
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        films = data.get('films', [])
        
        if films:
            info = []
            film = films[0]
            name = film.get('nameRu')
            year = film.get('year', 'Неизвестно')
            rating = film.get('rating') # Добавлено
            description = film.get('description', 'Отсутствует') # Добавлено
            if rating == 'null': # Добавлено
                rating = 'Неизвестно' # Добавлено

            if name:
                info.append(
                    f"{name}({year})\n"
                    f"⭐Рейтинг: {rating}\n"
                    f"📄Описание: {description}\n"
                )
            return "\n".join(info)
        else:
            return None
    else:
        return None
