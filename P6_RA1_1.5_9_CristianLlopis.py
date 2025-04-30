# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 29/04/2025

# Versió: 1.0

# Descripció(programa): Divideix una frase en paraules i les mostra una per una.

frase = input("Introdueix una frase: ")
paraules = frase.split()
for p in paraules:
    print(p)