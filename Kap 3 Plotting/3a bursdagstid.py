import matplotlib.pyplot as plt

kategorier = ["Q1", "Q2", "Q3", "Q4"]
verdier = [9, 5, 7, 10]

# Kan gi med farger til stolpene:
farger = ["blue", "green", "yellow", "brown"]

# Stolpediagram:
bars = plt.bar(kategorier, verdier, color=farger)

# Viser tallet (verdien) på toppen av søylene:
# Kompleks, manuell måte fra chat under her...
# plt.bar_label(bars)

# Endret: legg labels manuelt for mer kontroll
for bar in bars:
    h = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # x: midt på stolpen
        h,                                  # y: på toppen av stolpen
        f'{h}',                             # label-tekst
        ha='center', va='bottom',           # sentrert og plassert rett over stolpen
        fontsize=10
    )

# HUSK! Alltid show() til slutt for å se plottet:
plt.show()
