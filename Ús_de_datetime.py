# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025

# Versió: 1.0

# Descripció(programa): Mostra data actual i calcula dies fins Nadal

from datetime import datetime

ara = datetime.now()
print(ara.strftime("%d/%m/%Y %H:%M"))

nadal = datetime(ara.year, 12, 25)
dies_restants = (nadal - ara).days
print(f"Dies fins Nadal: {dies_restants}")
