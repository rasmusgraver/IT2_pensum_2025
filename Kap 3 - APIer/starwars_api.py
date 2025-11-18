import requests as req
from pprint import pprint

url = "https://swapi.dev/api/films/"

resultat = req.get(url)
print(f"Statuskode: {resultat.status_code}")

data = resultat.json()
pprint(data)
results = data["results"]
for result in results:
    episode = result["episode_id"]
    premiere_dato =  result["release_date"]
    tittel = result["title"]
    print(tittel, episode, premiere_dato)
    # TODO: Lag et StarWarsFilm-object med disse verdiene!

