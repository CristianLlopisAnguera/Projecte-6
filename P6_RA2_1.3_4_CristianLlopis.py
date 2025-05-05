# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025

# Versió: 1.0

# Descripció(programa): Compta i mostra quantes línies té un fitxer

with open('sortida.txt', 'r', encoding='utf-8') as fitxer:
    linies = fitxer.readlines()
    print(f"El fitxer té {len(linies)} línies.")
