# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025 

# Versió: 1.0

# Descripció(programa): Llegeix i mostra el contingut del fitxer missatge.txt

with open('missatge.txt', 'r', encoding='utf-8') as fitxer:
    contingut = fitxer.read()
    print(contingut)
