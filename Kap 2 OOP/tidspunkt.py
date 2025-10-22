import datetime as dt

class Tidspunkt:
  """
  Klasse for å lage tidspunkt-objekter.

  Parametre:
    tidsstempel = dt.datetime.now().timestamp() (int): tidspunktets tidsstempel
  """
  def __init__(self, tidsstempel = dt.datetime.now().timestamp()):
    """Konstruktør"""
    self.datotid = dt.datetime.fromtimestamp(tidsstempel)
  
  def tidsstempel(self):
    """Gir hele tidsstemplet"""
    return self.datotid

  def dato(self):
    """Gir dato på formen dd.mm.yyyy"""
    return self.datotid.strftime("%d.%m.%Y")

  def dag(self):
    """Gir datoens dag (01-31)"""
    return self.datotid.strftime("%d")

  def maaned(self):
    """Gir månedens fulle navn (på engelsk)"""
    return self.datotid.strftime("%B")
    
  def aar(self):
    """Gir årstall med fire siffer"""
    return self.datotid.strftime("%Y")

