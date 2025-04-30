# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 29/04/2025

# Versió: 1.0

# Descripció(programa): Demana un nombre enter i calcula la suma de tots els nombres des de 1 fins a aquest nombre. Gestiona errors.

try:
    numero = int(input("Introdueix un nombre enter positiu: "))
    if numero > 0:
        suma = sum(range(1, numero + 1))
        print(f"La suma dels nombres de 1 fins a {numero} és {suma}.")
    else:
        print("Has d'introduir un nombre enter positiu.")
except ValueError:
    print("Error: has d'introduir un nombre enter vàlid.")
