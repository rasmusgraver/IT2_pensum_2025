import  yatzy_utils as y

kast = y.nyttKast()
print(kast)
if type(kast) != list:
    print("FEIL! Nytt kast returnerte ikke en liste")
if len(kast) != 5:
    print("FEIL! Nytt kast returnerte 5 verdier")

fl = y.flestForekomster([1,2,4,5,1])
if fl != 1:
    print("FEIL! flestForekomster funka ikke:", fl)
else:
    print("flestForekomster er good")

kast = y.nullUt([1,2,4,5,1], 1)
if kast != [1,0,0,0,1]:
    print("FEIL! nullUt funka ikke", kast)
else:
    print("nullUt er good")

kast = y.reKast([1,0,0,0,1])
if kast.count(0) > 0:
    print("FEIL! reKast hadde nullere i seg:", kast)
elif kast[0] != 1:
    print("FEIL! Den skulle ikke fjernet første eneren")
elif kast[4] != 1:
    print("FEIL! Den skulle ikke fjernet andre eneren")
else:
    print("reKast er good")
