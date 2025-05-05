# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025

# Versió: 1.0

# Descripció(programa): Ús de la calculadora científica

import cientifica
import calculadora

print("1. Suma")
print("2. Resta")
print("3. Multiplicació")
print("4. Divisió")
print("5. Arrel quadrada")
print("6. Potència")
print("7. Seno")

opc = int(input("Tria una opció: "))

if opc == 1:
    a = float(input("a: "))
    b = float(input("b: "))
    print(calculadora.suma(a, b))
elif opc == 2:
    a = float(input("a: "))
    b = float(input("b: "))
    print(calculadora.resta(a, b))
elif opc == 3:
    a = float(input("a: "))
    b = float(input("b: "))
    print(calculadora.multiplicacio(a, b))
elif opc == 4:
    a = float(input("a: "))
    b = float(input("b: "))
    print(calculadora.divisio(a, b))
elif opc == 5:
    x = float(input("x: "))
    print(cientifica.arrel_quadrada(x))
elif opc == 6:
    x = float(input("base: "))
    y = float(input("exponent: "))
    print(cientifica.elevar(x, y))
elif opc == 7:
    x = float(input("angle (graus): "))
    print(cientifica.seno(x))
else:
    print("Opció no vàlida")
