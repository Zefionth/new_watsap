from openai import OpenAI
from config import OPENAI_API_TOKEN
from re import findall

# Инициализация клиента OpenAI с использованием API токена
client = OpenAI(
    api_key=f"{OPENAI_API_TOKEN}",
    base_url="https://api.proxyapi.ru/openai/v1",
)

def get_names(query: str, category: str) -> dict:
    """Получает названия фильмов или аниме по обобщенному описанию.

    Аргументы:
        query (str): Обобщенное описание для поиска.
        category (str): Категория поиска ('movies' или 'anime').

    Возвращает:
        dict: Словарь с названиями фильмов или аниме, или пустой словарь, если запрос непонятный.
    """
    # Формируем системное сообщение в зависимости от категории
    system_message = (
        "Пользователь хочет посмотреть фильмы по обобщенному описанию, аниме запрещены. До 5 штук. "
        "Отвечай в следующем виде словаря и никак иначе: "
        "{name_1: 'название фильма 1', name_2:'название фильма 2', и так далее}. "
        "Если запрос непонятный, нецензурный пиши {}"
    ) if category == 'movies' else (
        "Пользователь хочет посмотреть именно аниме по обобщенному описанию, До 5 штук. "
        "Отвечай в следующем виде словаря и никак иначе. Все названия на английском языке: "
        "{name_1: 'название аниме 1', name_2:'название аниме 2', и так далее}. "
        "Если запрос непонятный, нецензурный пиши {}"
    )

    # Выполняем запрос к модели OpenAI
    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": "Хочу посмотреть о:" + query}
        ]
    )

    # Извлекаем текст ответа и очищаем его от фигурных скобок
    response_text = chat_completion.choices[0].message.content.strip('{}')
    
    # Используем регулярные выражения для поиска ключей и значений в ответе
    pairs = findall(r'(\w+):\s*([^,]+)', response_text)
    
    # Создаем словарь из найденных пар ключ-значение
    result = {key: value.strip(" '") for key, value in pairs}
    
    return result