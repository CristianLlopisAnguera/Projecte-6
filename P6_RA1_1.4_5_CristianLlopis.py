# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 29/04/2025

# Versió: 1.0

# Descripció(programa): Imprimeix tots els nombres primers des de 2 fins a un nombre introduït per l’usuari. Gestiona errors.

def es_primer(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

try:
    numero = int(input("Introdueix un nombre enter positiu: "))
    if numero >= 2:
        print(f"Nombres primers de 2 a {numero}:")
        for i in range(2, numero + 1):
            if es_primer(i):
                print(i, end=' ')
    else:
        print("Has d'introduir un nombre major o igual a 2.")
except ValueError:
    print("Error: has d'introduir un nombre enter vàlid.")
