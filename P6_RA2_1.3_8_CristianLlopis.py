# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025 

# Versió: 1.0

# Descripció(programa): Llegeix nombres.txt i gestiona errors si alguna línia no és un enter

with open('nombres.txt', 'r', encoding='utf-8') as fitxer:
    for i, linia in enumerate(fitxer, start=1):
        try:
            num = int(linia.strip())
            print(f"Línia {i}: {num}")
        except ValueError:
            print(f"Error: La línia {i} no és un nombre enter vàlid.")
