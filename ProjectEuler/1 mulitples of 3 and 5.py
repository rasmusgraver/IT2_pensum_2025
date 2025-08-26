# https://projecteuler.net/problem=1


"""
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5,
 we get 3,5,6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

tot = 0

for i in range(1000):
    if i%3 == 0 or i%5 == 0:
        tot += i 

print(f"Sum av 3erne og 5erne er {tot}")


"""
Alternativ løsning: Legg sammen hvert 3. tall og hvert 5. tall
, MEN: Da har vi tatt de som er delelig på 15 dobbelt: Trekk fra dem :)
"""

tot = 0
for i in range(0,1000,3):
    tot += i
for i in range(0,1000,5):
    tot += i
for i in range(0,1000,15):
    tot -= i

print(f"Løsning 2: {tot}")
