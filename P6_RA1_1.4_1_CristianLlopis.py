# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 29/04/2025

# Versió: 1.0

# Descripció(programa): Utilitzant el range(), escriu un programa que generi una seqüència de nombres des de 0 fins a un nombre introduït per l'usuari. Gestiona errors.

try:
    numero = int(input("Introdueix un nombre enter: "))
    for i in range(num + 1):
        print(i, end=' ')
except ValueError:
    print("Error: has d'introduir un nombre enter vàlid.")
