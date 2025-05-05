# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025

# Versió: 1.0

# Descripció(programa): Funció recursiva que calcula el factorial d'un nombre

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
