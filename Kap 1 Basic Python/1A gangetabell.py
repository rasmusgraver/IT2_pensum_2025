
"""
# Demo av dobbel for-løkke, og også dette med end= til print:
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i*j:2}", end=" ")
    print()
"""

def skrivRad(tall):
    for i in range(tall, 10*tall+1, tall):
        if i < 10:
            print(" ", end="")
        print(i, end=" ")
    print()

# Skriv gangetabellen fra 1 til 9:
for t in range(1, 10):
    skrivRad(t)