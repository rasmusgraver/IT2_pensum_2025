
"""
Del 1: Oppgave 3 - Hva printes?
"""


# a) 2  (Siden i øker med 3 hver gang, så blir det ikke mer printing)
print("\n\n--- a)")
for i in range (2,5,3):
    print(i)

# b) 5    (t blir 3, og så 5 - printes bare til slutt)
print("\n\n--- b)")
t = 1
while t < 4:
    t += 2
print(t)

# c) 9 (1+3+5)
print("\n\n--- c)")
t = 0
for i in range(1,6,2):
    t += i
print(t)

# d) 0 1 0 1 0  (i er 0,1,2,3,4)
print("\n\n--- d)")
for i in range(5):
    print(i%2)


# e) 4  aa
print("\n\n--- e)")
def dobbel(a):
    return a+a
print(dobbel(2))
print(dobbel("a"))


# f) 1     [2, "hei", 4]
print("\n\n--- f)")
l = [1,2,"hei"]
l.append(4)
print(l.pop(0))
print(l)

# g) 1  (returnerer minste tallet fra lista)
print("\n\n--- g)")
def f(liste):
    a = liste[0]
    for t in liste:
        if t < a:
            a = t
    return a

print(f([2,4,1,6,4,9]))


# h) 0 0    1 1     2 2     3 3     4 4
print("\n\n--- h)")
for i in range(5):
    for j in range(i, 5):
        if i == j:
            print(i, j)


# i) False         True
print("\n\n--- i)")
a = 1
for i in range(2):
    print(a == i)

    
# j) Julenøtt. Tenk bakfra: 
#       f(1) = 1 
#       f(2) = 2 + 2*(1) = 4
#       f(3) = 3 + 2*(4) = 11  => Altså printer programmet 11
print("\n\n--- j)")
def f(x):
    if x <= 1:
        return 1
    return x + 2*f(x-1)

print(f(3))

