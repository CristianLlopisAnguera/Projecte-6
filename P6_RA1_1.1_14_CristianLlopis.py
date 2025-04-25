# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 25/04/2025

# Versió: 1.0

# Descripció(programa): Calcula el preu d’un producte amb IVA del 21%.

preu = float(input("Introdueix el preu del producte: "))
preu_final = preu * 1.21
print("El preu amb IVA és:", round(preu_final, 2))