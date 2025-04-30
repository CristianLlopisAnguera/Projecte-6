# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 29/04/2025

# Versió: 1.0

# Descripció(programa): Demana 5 paraules a l'usuari i emmagatzema-les en una llista.

paraules = []
for i in range(5):
    p = input(f"Introdueix la paraula {i+1}: ")
    paraules.append(p)
print("Paraules:", paraules)