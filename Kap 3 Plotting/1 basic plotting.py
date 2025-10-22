import matplotlib.pyplot as plt

xer = []
yer = []

def f(x):
    return x**2

for i in range(-10, 11):
    xer.append(i)
    yer.append(f(i))

# Legger til rutenett
plt.grid(True)

# Legger til aksetitler
plt.xlabel("x-akse")
plt.ylabel("y-akse")

# Legger til tittel på plottet
plt.title("Grafen til f(x) = x²")

plt.plot(xer, yer)
plt.scatter(xer, yer)
plt.show()

