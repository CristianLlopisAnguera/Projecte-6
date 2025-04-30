# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 29/04/2025

# Versió: 1.0

# Descripció(programa): Imprimeix tots els nombres parells des de 0 fins a un nombre introduït per l’usuari. Gestiona errors.

try:
    numero = int(input("Introdueix un nombre enter positiu: "))
    if numero >= 0:
        print(f"Nombres parells de 0 a {numero}:")
        for i in range(0, numero + 1, 2):
            print(i, end=' ')
    else:
        print("Has d'introduir un nombre positiu.")
except ValueError:
    print("Error: has d'introduir un nombre enter vàlid.")
