import shikimori_api
from re import sub

def format_year(year):
    """Форматирует год для отображения, заменяя '-' на '.' или возвращает 'онгоинг', если None."""
    return year.replace('-', '.') if year else 'онгоинг'

def clean_description(description):
    """Удаляет ненужные символы из описания и возвращает сообщение по умолчанию, если None."""
    return sub(r"[\(\[].*?[\)\]]", "", description) if description else 'Нет описания'

def get_info_anime(name: str) -> str:
    """Получает и форматирует информацию об аниме по его названию.

    Аргументы:
        name (str): Название аниме для поиска.

    Возвращает:
        str: Отформатированная строка с информацией об аниме или None, если не найдено.
    """
    # Создаем сессию с API Shikimori
    session = shikimori_api.Shikimori()
    api = session.get_api()
    
    # Ищем аниме по названию и получаем первый результат
    search_anime = api.animes.GET(search=name, kind='tv')[0]
    
    # Получаем подробную информацию об аниме по его ID
    anime = api.animes(search_anime['id']).GET()

    # Извлекаем необходимые данные из информации об аниме
    name = anime['russian']
    aired_year = format_year(anime['aired_on'])
    released_year = format_year(anime['released_on'])
    rating = anime['score']
    imageUrl = anime['image']['original']
    description = clean_description(anime['description'])

    # Проверяем, доступно ли название аниме, и форматируем вывод
    if name:
        return (
            f"{name}({aired_year} - {released_year})\n"
            f"⭐Рейтинг: {rating}\n"
            f"📄Описание: {description}\n"
            f"🖼️Постер: https://shikimori.one/{imageUrl}\n"
        )
    
    # Возвращаем None, если название не найдено
    return None