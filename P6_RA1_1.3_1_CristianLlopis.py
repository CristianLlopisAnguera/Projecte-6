# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 27/04/2025

# Versió: 1.0

# Descripció(programa): Genera una seqüència de nombres des de 0 fins a un nombre introduït per l'usuari

try:
    numero = int(input("Introdueix un nombre enter: "))
    for i in range(numero + 1):
        print(i)
except ValueError:
    print("Error: No has introduït un nombre enter vàlid.")