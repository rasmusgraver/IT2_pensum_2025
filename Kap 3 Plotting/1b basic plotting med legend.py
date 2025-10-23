import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2

def g(x):
    return x**3

# Mer kompakt måte å gjøre dette på ved hjelp av numpy:

# Oppretter 50 punkter mellom -10 og 10:
xer = np.linspace(-10, 10, 50)
# MERK: Kan bruke funksjonen med numpy array som argument! 
# Returnerer ny liste med y-verdiene:
xiannen = f(xer)
xitredje = g(xer)

# Tegner x og y aksen:
plt.axhline(y=0, color="green")
plt.axvline(x=0, color="green")

# Kan sette limit på x og y aksen:
plt.ylim(-30, 100)

# MERK: Kan gi med en label til plot!
plt.plot(xer, xiannen, label = "X i andre")
plt.plot(xer, xitredje, label = "X i tredje")

# HUSK! Må ha med denne for å vise labels:
plt.legend() # optional parameter "loc=" kan si "upper right" osv

# HUSK! Må alltid ha denne for å vise grafen!
plt.show()


