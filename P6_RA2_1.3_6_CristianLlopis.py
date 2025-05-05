# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025 

# Versió: 1.0

# Descripció(programa): Comprova si dades.txt existeix abans de llegir-lo

import os

if os.path.exists('dades.txt'):
    with open('dades.txt', 'r', encoding='utf-8') as fitxer:
        print(fitxer.read())
else:
    print("Error: El fitxer dades.txt no existeix.")
