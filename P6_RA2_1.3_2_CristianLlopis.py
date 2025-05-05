# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025 

# Versió: 1.0

# Descripció(programa): Escriu 3 línies en el fitxer sortida.txt (sobreescriu el contingut)

with open('sortida.txt', 'w', encoding='utf-8') as fitxer:
    fitxer.write("Primera línia\n")
    fitxer.write("Segona línia\n")
    fitxer.write("Tercera línia\n")
