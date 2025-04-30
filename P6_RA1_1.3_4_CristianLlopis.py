# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 27/04/2025

# Versió: 1.0

# Descripció(programa): Imprimeix tots els nombres parells des de 0 fins a un nombre introduït per l'usuari

try:
    numero = int(input("Introdueix un nombre enter positiu: "))
    if numero < 0:
        print("Error: Has d'introduir un nombre enter positiu.")
    else:
        for i in range(0, numero + 1, 2):
            print(i)
except ValueError:
    print("Error: No has introduït un nombre enter vàlid.")
