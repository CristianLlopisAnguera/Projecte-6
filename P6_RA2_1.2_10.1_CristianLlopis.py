# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025 

# Versió: 1.0

# Descripció(programa): Filtra els nombres parells de diferents llistes

def filtra_parells(llista):
    return [x for x in llista if x % 2 == 0]

print(filtra_parells([1, 2, 3, 4, 5, 6]))
print(filtra_parells([10, 15, 20, 25, 30]))
