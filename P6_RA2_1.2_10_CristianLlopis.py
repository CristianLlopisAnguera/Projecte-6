# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025 

# Versió: 1.0

# Descripció(programa): Funció que filtra i retorna només els nombres parells d'una llista

def filtra_parells(llista):
    return [x for x in llista if x % 2 == 0]
