# a oppgaven 
tall = [3, 7, 2, 9, 4, 6, 1, 8]
resultat = 0

for t in tall:
    if t % 2 == 0:
        resultat += t

print(resultat)
# Printer summen av partallene: 2+4+6+8 = 20

# b-oppgaven
x = 5

def test():
    global x
    x = 10

test()
print(x)
# printer 10 pga "global"