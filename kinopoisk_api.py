import requests
from config import KINOPOISK_API_TOKEN

def get_info_movies(name: str) -> str:
    """Получает и форматирует информацию о фильме по его названию.

    Аргументы:
        name (str): Название фильма для поиска.

    Возвращает:
        str: Отформатированная строка с информацией о фильме или None, если не найдено.
    """
    # Формируем URL для API КиноПоиск с указанным названием фильма
    url = f"https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword={name}"
    headers = {
        'X-API-KEY': KINOPOISK_API_TOKEN  # Заголовок с API ключом
    }
    
    # Выполняем GET-запрос к API
    response = requests.get(url, headers=headers)

    # Получаем данные из ответа в формате JSON
    data = response.json()
    films = data.get('films', [])  # Извлекаем список фильмов

    if films:
        film = films[0]  # Берем первый фильм из списка
        name = film.get('nameRu')  # Название фильма на русском
        year = film.get('year', 'Неизвестно')  # Год выпуска фильма
        imageUrl = film.get('posterUrl')  # URL постера фильма
        rating = film.get('rating')  # Рейтинг фильма
        description = film.get('description', 'Отсутствует')  # Описание фильма
        
        # Обработка случая, когда рейтинг равен 'null'
        if rating == 'null':
            rating = 'Неизвестно'

        if name:
            return (
                f"{name}({year})\n"
                f"⭐Рейтинг: {rating}\n"
                f"📄Описание: {description}\n"
                f"🖼️Постер: {imageUrl}\n"
            )
    
    # Возвращаем None, если фильмы не найдены
    return None
