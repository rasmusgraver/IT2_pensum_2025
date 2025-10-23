import matplotlib.pyplot as plt
import random

terningkast = []

for _ in range(100):
    terningkast.append(random.randint(1,6))

# Én stolpe per verdi 1-6, sentrert på heltall
plt.hist(terningkast, bins=[1,2,3,4,5,6,7], align='left', color="seagreen", edgecolor="black")
plt.xlabel("Terningkast")
plt.ylabel("Antall")

# Sett x-ticks, "midt på stolpene"
plt.xticks([1,2,3,4,5,6])

plt.show()