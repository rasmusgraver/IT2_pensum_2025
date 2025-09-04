# Sånn Aunivers gjorde det:
gyldig = False
while not gyldig:
  try:
    tall = int(input("Skriv et tall "))
    if tall >= 1 and tall <= 10:
      gyldig = True
  except ValueError:
    print("Du må skrive inn et heltall.")

print(f"Du skrev inn {tall}.")
