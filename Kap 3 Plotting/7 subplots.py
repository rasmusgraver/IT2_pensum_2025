import matplotlib.pyplot as plt

"""
Eksempel med "moderne måten" å lage subplots på (fra ChatGPT).

"""

# Lag et rutenett med 2 rader og 2 kolonner
fig, axs = plt.subplots(2, 2, figsize=(10, 6))

# Tegn fire grafer
axs[0, 0].scatter([1, 2, 3], [1, 2, 3])
axs[0, 0].set_title("Graf 1")

axs[0, 1].plot([1, 2, 3], [1, 4, 9])
axs[0, 1].set_title("Graf 2")

farger = ["brown", "purple", "pink"]
axs[1, 0].bar(["Hund", "Katt", "Kanin"], [3, 8, 5], color=farger)
axs[1, 0].set_title("Graf 3")

axs[1, 1].pie([13, 22, 11], labels = ["Is", "Kake", "Sjokolade"])
axs[1, 1].set_title("Graf 4")

# Gi litt luft mellom subplottene
plt.tight_layout()

plt.show()
