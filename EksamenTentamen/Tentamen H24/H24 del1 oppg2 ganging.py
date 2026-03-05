
"""
Del 1, oppgave 2 - ganging av tall
"""

ant = {
	1: 0,
	2: 0,
	3: 0,
	4: 0,
	5: 0
}
for i in range(10, 100):
	for j in range(10, 100):
		l = len(str(i*j))
		ant[l] += 1

"""
Del 1, oppgave 2 - ganging av tall

Svar: Programmet har funnet ut at hvis du ganger sammen alle
mulige kombinasjoner av 2 to-sifrede tall (10*10, 10*11, 11*10....98*99, 99*98, 99*99)
så vil du få et svar som er tre-sifret 1490 ganger og et fire-sifret svar 6610 ganger.
"""
