# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 27/04/2025

# Versió: 1.0

# Descripció(programa): Mostra la taula de multiplicar d'un número introduït per l'usuari

try:
    numero = int(input("Introdueix un nombre enter per veure la seva taula de multiplicar: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
except ValueError:
    print("Error: No has introduït un nombre enter vàlid.")