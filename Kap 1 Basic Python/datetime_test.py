from datetime import datetime

# Datoen jeg ble født:
datoStreng = "1978-11-16"
dato = datetime.strptime(datoStreng, "%Y-%m-%d")
# strptime betyr "string parse time" => gjør om en streng til dato objekt
print(dato)
ukedagIndex = dato.weekday()
print(ukedagIndex)

ukedager = ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"]
print("Du ble født på en", ukedager[ukedagIndex])


# Vi har også strftime - string format time => Gjør om en dato til en streng
# Husk altså: 
# - strftime - format time => fra dato til streng
# - strptime - parse  time => fra streng til dato

print(dato.strftime("år: %Y, måned: %m"))
# for en full liste av muligheter se her 
# https://www.w3schools.com/python/python_datetime.asp 

print("Du ble født på en", dato.strftime("%A"))


# Dagens dato med now():
naa = datetime.now()

# Kan ta differansen mellom 2 datoer: 
diff = naa - dato

# Da får vi et timedelta objekt:
print("Diff type:", type(diff))

# som har ulike atributter:
print("Antall dager:", diff.days)

