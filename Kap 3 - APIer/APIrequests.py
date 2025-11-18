import requests as req
from pprint import pprint 

# tall = input(....) .... 
url = "http://numbersapi.com/100?json"

resultat = req.get(url)

print(f"Statuskode: {resultat.status_code}")

data = resultat.json()
pprint(data)
print(data["text"])








# jsonTxt = resultat.json()
# pprint(jsonTxt)
#data = json.loads(resultat.content)