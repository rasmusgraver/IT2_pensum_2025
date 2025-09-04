# Spør brukeren om et tall mellom 1 og 10
# (fra og med, til og med)
# Fortsett å spør intil brukeren svarer med
# et gyldig tall
tall = 0
while tall < 1 or tall > 10:
    try:
      tall = int(input("Gi meg et tall mellom 1 og 10: "))
    except ValueError:
       print("Du må skrive et heltall")
       tall = 0 # Fortsett å spør

print(f"Du skrev {tall}")


