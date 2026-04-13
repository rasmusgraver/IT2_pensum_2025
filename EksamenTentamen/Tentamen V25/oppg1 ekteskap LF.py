class Person():
  def __init__(self,navn):
    self.navn = navn
    self.ektefelle = None
    self.barn = None

  def __repr__(self):
    return self.navn

  def visStatus(self):
    if self.ektefelle:
      print(f"Jeg er gift med {self.ektefelle}.")
    else:
      print("Jeg er singel.")

  def gifteMeg(self,ektefelleObjekt):
    if self.ektefelle:
      print(f"{self} er allerede gift med {self.ektefelle}.")
    elif ektefelleObjekt.ektefelle:
      print(f"{ektefelleObjekt} er allerede gift med {ektefelleObjekt.ektefelle}.")
    else:
      self.ektefelle = ektefelleObjekt
      ektefelleObjekt.ektefelle = self
  
  def faaBarn(self,barnNavn):
    if self.ektefelle:
      self.barn = Person(barnNavn)
      self.ektefelle.barn = self.barn
      print(f"{self} og {self.ektefelle} har fått barn: {self.barn}.")
    else:
      print(f"{self.navn} er singel og kan ikke få barn.")

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
