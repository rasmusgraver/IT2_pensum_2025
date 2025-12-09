from parkering import Bil, Parkeringshus

# Opprett parkeringshus med plass til 5 biler:
parkering = Parkeringshus(5)

# Opprett noen biler
bil1 = Bil("rød", "Tesla", "AB12345")
bil2 = Bil("blå", "BMW", "CD67890")
bil3 = Bil("hvit", "Volvo", "EF11111")
bil4 = Bil("svart", "Audi", "GH22222")
bil5 = Bil("grønn", "Mercedes", "IJ33333")
bil6 = Bil("gul", "Toyota", "KL44444")

# Test: Parker 5 biler (skal fungere)
print("=== Parker 5 biler ===")
print(f"Parker bil1: {parkering.parkerBil(bil1)}")
print(f"Parker bil2: {parkering.parkerBil(bil2)}")
print(f"Parker bil3: {parkering.parkerBil(bil3)}")
print(f"Parker bil4: {parkering.parkerBil(bil4)}")
print(f"Parker bil5: {parkering.parkerBil(bil5)}")

# Test: Parker 6. bil (skal feile - fullt)
print("\n=== Prøv å parker 6. bil (fullt) ===")
print(f"Parker bil6: {parkering.parkerBil(bil6)}")

# Test: Prøv å parker samme bil igjen (skal feile)
print("\n=== Prøv å parker samme bil igjen ===")
print(f"Parker bil1 igjen: {parkering.parkerBil(bil1)}")

# Test: List farger
print("\n=== Liste farger ===")
farger = parkering.listFarger()
print(f"Farger på parkerte biler: {farger}")

# Test: Hent ut bil
print("\n=== Hent ut bil ===")
hentet = parkering.hentUtBil("AB12345")
print(f"Hentet bil: {hentet}")

# Test: Prøv å hente ut bil som ikke er der
print("\n=== Prøv å hente ut bil som ikke er der ===")
hentet = parkering.hentUtBil("AB12345")
print(f"Hentet bil: {hentet}")

# Test: List farger etter at en bil er hentet ut
print("\n=== Liste farger etter henting ===")
farger = parkering.listFarger()
print(f"Farger på parkerte biler: {farger}")