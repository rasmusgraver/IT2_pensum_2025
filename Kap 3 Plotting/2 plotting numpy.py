import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2

xer = np.linspace(-10, 10, 50)
yer = f(xer)

plt.grid(True)
plt.xlabel("x-akse")
plt.ylabel("y-akse")
plt.title("Grafen til f(x) = x²")

# Du kan bruke fargenavn
plt.plot(xer, yer, color='red')
# Eller RGB-kode
# plt.plot(xer, yer, color='#FF0000')
# Eller forkortelser
# plt.plot(xer, yer, 'r')

plt.show()


