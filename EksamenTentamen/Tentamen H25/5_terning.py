import matplotlib.pyplot as plt
import random

def terningSum(antall:int):
    tot = 0
    for _ in range(antall):
        tot += random.randint(1,6)
    return tot

kast = []
antallTerninger = int(input("Hvor mange terninger? "))
for _ in range(500):
    kast.append(terningSum(antallTerninger))

# plt.hist(kast)
plt.hist(kast, bins=11, edgecolor='black', density=True)
plt.xlabel("Sum")
plt.ylabel('Frekvens')
plt.title(f"Histogram av {antallTerninger} terninger")

plt.show()
