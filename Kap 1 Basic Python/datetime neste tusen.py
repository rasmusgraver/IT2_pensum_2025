from datetime import datetime, timedelta

bok = {
    "Anders": "1990-07-12",
    "Rasmus": "1978-11-16",
    "Arne": "1985-12-30",
    "Erik": "1990-06-05"
}

# Dagens dato med now():
naa = datetime.now()

for person, datoStr in bok.items():
    dato = datetime.strptime(datoStr, "%Y-%m-%d")
    print(person, "Du ble født på en", dato.strftime("%A"))

    # Kan ta differansen mellom 2 datoer: 
    diff = naa - dato

    # Da får vi et timedelta objekt:
    # print("Diff type:", type(diff))


    nesteTusen = 1000 - (diff.days % 1000)

    # print("Neste tusen", nesteTusen)

    print(person, "Du blir", diff.days + nesteTusen, "dager den", (naa + timedelta(days=nesteTusen)).strftime("%Y-%m-%d"))
    # som har ulike atributter:
    print("- Antall dager:", diff.days)
