import matplotlib.pyplot as plt

country = [
  "China", "Japan", "Germany", "USA", "South Korea", "India", "Spain", "Mexico", "Brazil", "UK"
]

cars_produced = [
  24420744, 7873886, 5746808, 3934357, 3859991, 3677605, 2354117, 1993168, 1778464, 1722698
]

# Konverterer til millioner
cars_produced_millions = [x / 1_000_000 for x in cars_produced]

# Definerer farger for hver søyle
colors = ['blue', 'orange', 'green', 'red', 'purple', 'cyan', 'magenta', 'yellow', 'brown', 'pink']

# Plotter stolpene med zorder for å ligge over grid-linjene
plt.bar(country, cars_produced_millions, color=colors, zorder=2)  # Bruker fargene

# Legger til horisontale linjer
plt.grid(axis='y')  # Legger til gridlinjer for y-aksen

# Vri etikettene 90 grader
plt.xticks(rotation=90)

# Legger til aksetittel for y-aksen
plt.ylabel("Biler produsert (millioner)")

# Bruk tight layout
plt.tight_layout()

plt.show()


