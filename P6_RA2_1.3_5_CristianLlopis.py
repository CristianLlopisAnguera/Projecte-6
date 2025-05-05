# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025 

# Versió: 1.0

# Descripció(programa): Llegeix i mostra el fitxer, i afegeix una línia al final en mode r+

with open('sortida.txt', 'r+', encoding='utf-8') as fitxer:
    contingut = fitxer.read()
    print(contingut)
    fitxer.write("Línia afegida en mode r+.\n")