from shikimori_api import Shikimori

def get_info_python
    anime_name = input('введите название аниме : ')

    session = Shikimori()
    api = session.get_api()
    search_anime = api.animes.GET(search=anime_name, kind='tv')[0]
    anime = api.animes(search_anime['id']).GET()

    russian_name = anime['russian']
    rating = anime['score']
    image_url = anime['image']['original']
    russian_genres = [genre['russian'] for genre in anime['genres']]
    russian_description = anime['description']

    print(anime)
    print("Название Аниме:", russian_name)
    print("Рейтинг: ", rating)
    print(f"Жанры : {', '.join(russian_genres)}")
    print("Ссылка на постер: "+"https://shikimori.one/"+image_url)
print("Описание: " +russian_description)
