# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025 

# Versió: 1.0

# Descripció(programa): Intenta escriure en resultats.txt i gestiona PermissionError

try:
    with open('resultats.txt', 'w', encoding='utf-8') as fitxer:
        fitxer.write("Escrivint resultats...\n")
except PermissionError:
    print("No tens permisos per escriure al fitxer resultats.txt.")
