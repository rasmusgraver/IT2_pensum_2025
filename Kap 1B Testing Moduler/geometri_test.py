from geometri_utils import arealAvSirkel

areal = arealAvSirkel(2)
print(areal)
if areal != (3.14*4):
    print("FEIL. Areal av sirkel med r=2")

areal = arealAvSirkel(1)
print(areal)
if areal != (3.14):
    print("FEIL. Areal av sirkel med r=1")

    