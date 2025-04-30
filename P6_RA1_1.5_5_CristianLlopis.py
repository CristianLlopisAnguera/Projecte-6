# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 29/04/2025

# Versió: 1.0

# Descripció(programa): Substitueix totes les lletres 'a' per '@' en una frase.

frase = input("Introdueix una frase: ")
nova_frase = frase.replace('a', '@').replace('A', '@')
print(nova_frase)