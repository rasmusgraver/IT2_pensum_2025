import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2

def g(x):
    return x**3

xer = np.linspace(-10, 10, 50)
yer = f(xer)
yer2 = g(xer)


# Setter størrelse på lerretet
plt.figure(figsize=(10, 6))

# Legger til rutenett
plt.grid(True)

# Markerer x og y aksen med svarte linjer
plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black')

# Legger til aksetitler
plt.xlabel("x-akse")
plt.ylabel("y-akse")

# Legger til tittel på plottet
plt.title("Sammenligning av funksjoner")

# Plotter begge funksjonene
plt.plot(xer, yer, color='blue', linestyle='--', label='f(x) = x²')
plt.plot(xer, yer2, color='green', label='g(x) = x³')
plt.scatter(xer, yer, color='red', marker='o')

# Setter grenser for aksene
plt.ylim(-50, 70)
plt.xlim(-9, 9)

# Legger til forklaringsboks
plt.legend()

plt.show()

