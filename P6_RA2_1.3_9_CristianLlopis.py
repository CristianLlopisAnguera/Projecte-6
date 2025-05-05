# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025 

# Versió: 1.0

# Descripció(programa): Obre un fitxer en mode lectura; si no existeix, el crea

try:
    with open('exemple.txt', 'r', encoding='utf-8') as fitxer:
        print(fitxer.read())
except FileNotFoundError:
    with open('exemple.txt', 'w', encoding='utf-8') as fitxer:
        fitxer.write("Fitxer creat automàticament.\n")
    print("El fitxer no existia. S'ha creat amb contingut per defecte.")
