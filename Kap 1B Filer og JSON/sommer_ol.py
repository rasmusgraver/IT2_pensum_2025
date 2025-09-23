import json
from pprint import pprint

filnavn = 'DataFiler/sommer_ol.json'
# For filer med norske tegn
with open(filnavn, 'r', encoding='utf-8') as f:
    data = json.load(f)


# Legg merke til pprint! (og hvordan importere den)
pprint(data)

# TODO: Print årstallene/vinnertidene på egne rader for hver
# Challenge: Sortere etter årstall:
#   - lag en ny ordbok der årstaller er key
#   - lag en liste med alle alle keys (årstallene)
#   - sorter den lista, og bruk det til å printe det ut pent kronologisk 