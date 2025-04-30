# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 27/04/2025

# Versió: 1.0

# Descripció(programa): Calcula la suma de tots els nombres des de 1 fins a un nombre introduït per l'usuari

try:
    numero = int(input("Introdueix un nombre enter positiu: "))
    if numero < 1:
        print("Error: Has d'introduir un nombre enter positiu.")
    else:
        suma = sum(range(1, numero + 1))
        print(f"La suma de 1 fins a {numero} és: {suma}")
except ValueError:
    print("Error: No has introduït un nombre enter vàlid.")