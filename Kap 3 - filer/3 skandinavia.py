import json
from pprint import pprint 


filnavn = "DataFiler/skandinavia.json"

with open(filnavn, encoding="utf-8") as f:
  data = json.load(f)


data_formatert = json.dumps(data, indent=2,ensure_ascii=False)
print(data_formatert)

for land in data["land"]:
  print(land["navn"])

