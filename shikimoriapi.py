import shikimori_api
from re import sub

def get_info_anime(name: str) -> str:

    session = shikimori_api.Shikimori()
    api = session.get_api()
    search_anime = api.animes.GET(search=name, kind='tv')[0]
    anime = api.animes(search_anime['id']).GET()

    info = []
    name = anime['russian']
    aired_year = anime['aired_on']
    released_year = anime['released_on']
    if released_year == None:
        released_year = 'онгоинг'
    rating = anime['score']
    imageUrl = anime['image']['original']
    description = anime['description']
    if description == None:
        description = 'Нет описания'
    else:
        description = sub(r"[\(\[].*?[\)\]]", "", description)

    if name:
        info.append(
            f"{name}({aired_year.replace('-', '.')} - {released_year.replace('-', '.')})\n"
            f"⭐Рейтинг: {rating}\n"
            f"📄Описание: {description}\n"
            f"🖼️Постер: https://shikimori.one/{imageUrl}\n"
        )
        return "\n".join(info)
    else:
        return None
