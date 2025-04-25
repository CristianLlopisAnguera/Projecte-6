# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 25/04/2025

# Versió: 1.0

# Descripció(programa): 

import math

PI = 3.1416  # Constant

def calcular_area(radi):  # Aquesta part és una funció
    return PI * radi ** 2

radi = float(input("Introdueix el radi: "))  # Aquesta línia llegeix dades de l’usuari
area = calcular_area(radi)  # Variables: radi, area
print("L'àrea del cercle és:", area)  # Aquesta línia mostra el resultat