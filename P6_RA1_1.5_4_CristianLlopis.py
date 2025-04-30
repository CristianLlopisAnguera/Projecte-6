# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 29/04/2025

# Versió: 1.0

# Descripció(programa): Verifica si una paraula és un palíndrom.

paraula = input("Introdueix una paraula: ")
if paraula == paraula[::-1]:
    print("És un palíndrom.")
else:
    print("No és un palíndrom.")