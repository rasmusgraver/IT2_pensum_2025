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
    # OG: Lagre disse i en liste av filmer.
    # Fancy: Hent inn noen av personene også (fra de URLene du får fra APIet i "characters"),
    # lag objekter av disse også. Kanskje de skal i en ordbok, så du kan slå opp i den og se om personen
    # allerede har blitt "fetched"?

