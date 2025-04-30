# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 29/04/2025

# Versió: 1.0

# Descripció(programa): Elimina tots els espais d'una cadena.

def elimina_espais(cadena):
    return cadena.replace(" ", "")

text = input("Introdueix una cadena: ")
print("Sense espais:", elimina_espais(text))