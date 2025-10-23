import matplotlib.pyplot as plt

partiforkortelser = ["AP", "FrP", "H", "KrF", "MDG", "R", "Sp", "SV", "V", "PF"]
representanter = [48, 21, 36, 3, 3, 8, 28, 13, 8, 1]

plt.pie(representanter, labels=partiforkortelser)

plt.show()
