import matplotlib.pyplot as plt
import textwrap

utdanningsprogram = [
  "Bygg- og anleggsteknikk", 
  "Elektro og datateknologi",
  "Helse- og oppvekstfag",
  "Naturbruk",
  "Restaurant- og matfag",
  "Teknologi- og industrifag",
  "Håndverk, design og produktutvikling",
  "Frisør, blomster, interiør og eksponeringsdesign",
  "Informasjonsteknologi og medieproduksjon",
  "Salg, service og reiseliv"
]

antall = [3811, 4168, 8661, 2057, 1484, 5501, 313, 901, 1309, 2061]

# Bryt lange labels automatisk (bredde i tegn kan justeres)
wrapped = [textwrap.fill(s, width=18) for s in utdanningsprogram]

# Øk figurstørrelse
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(wrapped, antall, color='tab:blue')

# Roter fortsatt litt for bedre lesbarhet hvis ønskelig
plt.xticks(rotation=45, ha='center')

# Unngå at etiketter klippes
plt.tight_layout()

plt.show()