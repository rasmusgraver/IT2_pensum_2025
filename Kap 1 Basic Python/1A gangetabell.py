

# Demo av dobbel for-løkke, og også dette med end= til print:
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i*j:2}", end=" ")
    print()
