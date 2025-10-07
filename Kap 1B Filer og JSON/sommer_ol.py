import json
from pprint import pprint

# MERK: Filnavn er i forhold til hvor du står i terminalen! (Hvilken mappe du har åpnet i VS code)
filnavn = 'DataFiler/sommer_ol.json'
# Bruker utf-8 for å få inn norske tegn rett. 
with open(filnavn, 'r', encoding='utf-8') as f:
    data = json.load(f)


# Legg merke til pprint! (og hvordan importere den)
pprint(data)

# TODO: Hent ut vinnertidene til året 2020 (rad 2)

# TODO: Hent ut vinnertiden til 100 m for 2020

# TODO: Print årstallene/vinnertidene på egne rader for hver

# TODO: Challenge: Sortere etter årstall:
#   - lag en ny ordbok der årstaller er key
#   - lag en liste med alle alle keys (årstallene)
#   - sorter den lista, og bruk det til å printe det ut pent kronologisk 