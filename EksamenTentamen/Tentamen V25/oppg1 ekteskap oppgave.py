# Din kode her:



# Test av koden:
def hovedprogram():
  brad = Person("Brad Pitt")
  print("Brad status:")
  brad.visStatus()    # Jeg er singel.

  angie = Person("Angelina Jolie")
  brad.gifteMeg(angie)
  print("Brad status etter angie:")
  brad.visStatus()    # Jeg er gift med Angelina Jolie.

  cameron = Person("Cameron Diaz")
  print("Brad gifte meg cameron:")
  brad.gifteMeg(cameron)   # Brad Pitt er allerede gift med Angelina Jolie.

  print("Cameron gifte meg Brad:")
  cameron.gifteMeg(brad)   # Brad Pitt er allerde gift med Angelina Jolie.
  print("cameron status:")
  cameron.visStatus()      # Jeg er singel.

  print("cameron faaBarn:")
  cameron.faaBarn("Rosa Diaz")   # Cameron Diaz er singel og kan ikke få barn.
  print("angie faaBarn:")
  angie.faaBarn("Rosa Jolie-Pitt")   # Angelina Jolie og Brad Pitt har fått barn: Rosa Jolie-Pitt.

  print(f"Barnet til brad og angie er {brad.barn}.") # Barnet til brad og angie er Rosa Jolie-Pitt.
  print(f"Som er samme som {angie.barn}.") # Som er samme som Rosa Jolie-Pitt.

# Kaller på hovedprogrammet:
hovedprogram()
