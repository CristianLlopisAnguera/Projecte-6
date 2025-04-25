# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 25/04/2025

# Versió: 1.0

# Descripció(programa): Converteix minuts a hores i minuts.

minuts = int(input("Introdueix el nombre de minuts: "))
hores = minuts // 60
restants = minuts % 60
print(f"{minuts} minuts són {hores} hores i {restants} minuts.")
