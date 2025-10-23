import matplotlib.pyplot as plt
import numpy as np

partiforkortelser = ["AP", "FrP", "H", "KrF", "MDG", "R", "Sp", "SV", "V", "PF"]
representanter = [48, 21, 36, 3, 3, 8, 28, 13, 8, 1]

# Farger for hvert segment
colors = plt.cm.Paired(np.arange(len(partiforkortelser)))

# Lager pie-diagrammet (uten 3D-effekt)
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))
wedges, texts, autotexts = ax.pie(
    representanter,
    labels=partiforkortelser,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    shadow=False  # eksplisitt ingen skygge/3D
)


# Legger til legende
ax.legend(wedges, partiforkortelser, title="Partier", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Tittel
plt.title("Representasjon av partier i prosent", fontsize=16)

# Justerer layout
plt.tight_layout()

plt.show()
