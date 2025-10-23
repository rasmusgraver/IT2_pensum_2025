import matplotlib.pyplot as plt
import numpy as np

partiforkortelser = ["AP", "FrP", "H", "KrF", "MDG", "R", "Sp", "SV", "V", "PF"]
representanter = [48, 21, 36, 3, 3, 8, 28, 13, 8, 1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))

farger = ["#f58c68", "#004281", "#3396d2", "#d2bc2a", "#25a23c", "#5d0008", "#90cc93", "#d34d2f", "#005245", "#f69465"]

# Bruk colormap direkte og vis både prosent og antall i autopct
total = sum(representanter)
ax.pie(
    representanter,
    labels=partiforkortelser,
    colors=farger,
    autopct='%1.1f%%',
    startangle=90,
    labeldistance=1.15,
    wedgeprops = { "linewidth": 1, "edgecolor": "white" }
)

# Legg til legend hvis du vil ha samleforklaring ved siden av
ax.legend(partiforkortelser, title="Partier", loc="center left", bbox_to_anchor=(1, 0, 0.3, 1))

plt.title("Representasjon av partier", fontsize=14)
plt.tight_layout()
plt.show()
