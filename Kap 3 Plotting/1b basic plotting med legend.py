import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2

def g(x):
    return x**3






xer = np.linspace(-10, 10, 50)
xiannen = f(xer)
xitredje = g(xer)






plt.axhline(y=0, color="green")
plt.axvline(x=0, color="green")




plt.ylim(-30, 100)

# Linjeplot - bruker bare "plot"
plt.plot(xer, xiannen, label = "X i andre")
plt.plot(xer, xitredje, label = "X i tredje")

plt.legend()

# HUSK! Må alltid ha denne for å vise grafen!
plt.show()


