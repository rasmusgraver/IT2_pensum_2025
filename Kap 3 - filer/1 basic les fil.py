import matplotlib.pyplot as plt 

aarstall = []
valgdeltakelse = []
with open("DataFiler/valgdeltagelse.txt", encoding="utf-8") as fil:
    for linje in fil:
        verdier = linje.strip().split(";")
        aarstall.append(  verdier[0]   )
        valgdeltakelse.append(   float(verdier[1].replace(",", ".")  ) )


plt.plot(aarstall, valgdeltakelse)
plt.xticks(rotation=50, fontsize=8 )
plt.show()
