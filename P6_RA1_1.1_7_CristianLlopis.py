# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 25/04/2025

# Versió: 1.0

# Descripció(programa): Fa la resta, multiplicació i divisió de dos números.

numero1 = float(input("Introdueix el primer número: "))
numero2 = float(input("Introdueix el segon número: "))

print("La resta és:", numero1 - numero2)
print("La multiplicació és:", numero1 * numero2)

if numero2 != 0:
    print("La divisió és:", numero1 / numero2)
else:
    print("No es pot dividir per zero.")