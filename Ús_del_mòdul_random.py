# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025

# Versió: 1.0

# Descripció(programa): Simula llençar un dau i calcula la mitjana

import random

def llençar_dau():
    return random.randint(1, 6)

def llençar_n_daus(n):
    total = 0
    for _ in range(n):
        tirada = llençar_dau()
        print(f"Tirada: {tirada}")
        total += tirada
    return total / n

print(f"Mitjana de 10 tirades: {llençar_n_daus(10)}")
