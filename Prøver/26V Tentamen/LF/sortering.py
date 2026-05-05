# Bubble Sort - Sorteringsalgoritme

def sorter(liste):
    """
    Implementerer Bubble Sort algoritmen.
    Parametrer: liste - listen som skal sorteres
    Returner: den sorterte listen og antallet bytter som ble utført
    """
    # Vi jobber med en kopi av listen for ikke å endre originalen
    result = liste.copy()
    bytter_total = 0
    n = len(result)
    
    # Ytre løkke - kjører til ingen bytter finner sted
    bytter_denne_runden = 1
    runde = 0
    
    while bytter_denne_runden > 0:
        bytter_denne_runden = 0
        runde += 1
        
        # Indre løkke - går gjennom listen og sammenligner nabo-elementer
        for i in range(n - 1):
            if result[i] > result[i + 1]:
                # Bytt plass
                result[i], result[i + 1] = result[i + 1], result[i]
                bytter_denne_runden += 1
                bytter_total += 1
    
    return result, bytter_total, runde


# Test a) - Implementasjonen
print("=" * 60)
print("OPPGAVE a) Implementering av Bubble Sort")
print("=" * 60)

# Test c) - Med de to listene
liste1 = [5, 3, 8, 1, 9, 2]
liste2 = [1, 2, 3, 4, 5]

print("\nTest 1 - Usortert liste:")
print(f"Original liste: {liste1}")
resultat1, bytter1, runder1 = sorter(liste1)
print(f"Sortert liste:  {resultat1}")

print("\n" + "-" * 60)
print("OPPGAVE b) Antall bytter")
print("-" * 60)
print(f"Antall bytter utført: {bytter1}")
print(f"Antall runder: {runder1}")

print("\n" + "=" * 60)
print("Test 2 - Allerede sortert liste:")
print("=" * 60)
print(f"Original liste: {liste2}")
resultat2, bytter2, runder2 = sorter(liste2)
print(f"Sortert liste:  {resultat2}")
print(f"Antall bytter utført: {bytter2}")
print(f"Antall runder: {runder2}")

print("\n" + "=" * 60)
print("OPPGAVE c) Kommentar til kjøretiden")
print("=" * 60)
print(f"""
Test 1: [5, 3, 8, 1, 9, 2]
  - Antall bytter: {bytter1}
  - Antall runder: {runder1}
  - Kommentar: Listen er usortert, så algoritmen trenger flere runder
    for å sortere alle elementer riktig. Hver runde gjennomgår listen
    og bytter elementer som er i feil rekkefølge.

Test 2: [1, 2, 3, 4, 5]
  - Antall bytter: {bytter2}
  - Antall runder: {runder2}
  - Kommentar: Listen er allerede sortert. Algoritmen gjør kun én runde
    gjennom listen uten noen bytter, så den stopper umiddelbart.
    Dette viser at Bubble Sort har best-case på O(n).
""")

print("\n" + "=" * 60)
print("KJØRETIDSANALYSE")
print("=" * 60)
print("""
Bubble Sort kjøretid:
- Best case: O(n) - når listen allerede er sortert
- Average case: O(n²) - typisk for tilfeldig sortert liste
- Worst case: O(n²) - når listen er sortert i omvendt rekkefølge

For listen [5, 3, 8, 1, 9, 2] trengs det flere runder fordi elementer
må "boble" seg opp til riktig posisjon. Algoritmen må gjøre mange
sammenligninger og bytter.

For listen [1, 2, 3, 4, 5] trengs det kun én runde, siden listen
allerede er sortert fra starten.
""")
