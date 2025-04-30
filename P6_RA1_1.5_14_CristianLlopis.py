# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 29/04/2025

# Versió: 1.0

# Descripció(programa): Demana 10 números i crea dues llistes: parells i senars.

parells = []
senars = []

for _ in range(10):
    n = int(input("Introdueix un número: "))
    if n % 2 == 0:
        parells.append(n)
    else:
        senars.append(n)

print("Parells:", parells)
print("Senars:", senars)