import matplotlib.pyplot as plt

# pip3.14 install matplotlib
# pip3.14 install numpy 
# pip3.14 install pygame

xer = [1,2,3]
yer = [2,4,6]

# Helt basic plotting:

# linje:
plt.plot(xer, yer)

# punkter:
plt.scatter(xer, yer)

# HUSK! Alltid ha med show() til slutt (for å vise plottet) !
plt.show()

