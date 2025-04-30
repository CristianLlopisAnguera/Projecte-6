# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 29/04/2025

# Versió: 1.0

# Descripció(programa): Escriu una funció que reverteixi una cadena.

def reverteix(cadena):
    return cadena[::-1]

text = input("Introdueix una cadena: ")
print("Cadena invertida:", reverteix(text))