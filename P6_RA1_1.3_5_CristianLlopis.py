# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 29/04/2025

# Versió: 1.0

# Descripció(programa): Demana a l'usuari un número enter positiu i determina si és un nombre primer o no

numero = int(input("Introdueix un número enter positiu: "))
if numero > 1:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print(f"{numero} no és un nombre primer.")
            break
    else:
        print(f"{numero} és un nombre primer.")
else:
    print("Has d'introduir un número més gran que 1.")
