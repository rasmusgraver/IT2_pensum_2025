# TEST: Gi med end=... til print kommandoen
# print 1,3,5,7,...,21
for i in range(1,22,2):
    print(i, end="|")
print()
# print 5,9,13,17
for i in range(5,18,4):
    print(i)

# print 99,97,95,93,..., -1
for i in range(99, -2, -2):
    print(i)
