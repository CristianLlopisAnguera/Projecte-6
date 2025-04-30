# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 29/04/2025

# Versió: 1.0

# Descripció(programa): Mostra la taula de multiplicar d’un número introduït per l’usuari. Gestiona errors.

try:
    numero = int(input("Introdueix un nombre enter per veure la seva taula de multiplicar: "))
    print(f"Taula de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
except ValueError:
    print("Error: has d'introduir un nombre enter vàlid.")
