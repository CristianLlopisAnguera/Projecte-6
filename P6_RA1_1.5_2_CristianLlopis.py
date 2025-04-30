# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 29/04/2025

# Versió: 1.0

# Descripció(programa): Demana una frase i compta quantes vocals conté.

frase = input("Introdueix una frase: ")
vocals = "aeiouAEIOU"
compte = sum(1 for lletra in frase if lletra in vocals)
print(f"La frase conté {compte} vocals.")