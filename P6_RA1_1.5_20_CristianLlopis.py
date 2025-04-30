# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 29/04/2025

# Versió: 1.0

# Descripció(programa): Demana una llista de paraules i crea una nova llista amb les que comencen per vocal.

paraules = input("Introdueix paraules separades per espai: ").split()
vocals = "aeiouAEIOU"
comencen_vocal = [p for p in paraules if p[0] in vocals]
print("Paraules que comencen per vocal:", comencen_vocal)