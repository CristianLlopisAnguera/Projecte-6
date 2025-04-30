# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 29/04/2025

# Versió: 1.0

# Descripció(programa): Compta quantes vegades apareix una lletra concreta.

text = input("Introdueix una cadena: ")
lletra = input("Quina lletra vols comptar?: ")
comptador = text.count(lletra)
print(f"La lletra '{lletra}' apareix {comptador} vegades.")