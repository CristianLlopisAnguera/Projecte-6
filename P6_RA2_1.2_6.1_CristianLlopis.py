# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025 

# Versió: 1.0

# Descripció(programa): Multiplica diferents conjunts de nombres

def multiplica_tot(*nombres):
    resultat = 1
    for numero in nombres:
        resultat *= numero
    return resultat

print(multiplica_tot(2, 3, 4))
print(multiplica_tot(5, 10))
