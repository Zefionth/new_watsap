from openai import OpenAI
from config import OPENAI_API_TOKEN
from re import findall

client = OpenAI(
    api_key=f"{OPENAI_API_TOKEN}",
    base_url="https://api.proxyapi.ru/openai/v1",
)

def get_names(query: str) -> str:
    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
        {
            "role": "system",
            "content": "Пользователь хочет посмотреть фильмы, До 10 штук. "
                "Отвечай в следующем виде словаря и никак иначе: "
                "{name_1: 'название фильма 1', name_2:'название фильма 2', и так далее}. "
                "Если запрос непонятный, несвязный, пиши {}"
        },
        {"role": "user", "content": query}
        ]
    )
    response_text = chat_completion.choices[0].message.content.strip('{}') # получение именно ответа в виде строки 'key: value,'
    pairs = findall(r'(\w+):\s*([^,]+)', response_text) # использование регулярных выражений для поиска ключей и значений
    result = {key: value.strip(" '") for key, value in pairs} # создание словаря
    return result