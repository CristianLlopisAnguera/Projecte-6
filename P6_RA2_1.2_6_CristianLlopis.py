# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025 

# Versió: 1.0

# Descripció(programa): Funció que multiplica tots els nombres rebuts com a paràmetres

def multiplica_tot(*nombres):
    resultat = 1
    for numero in nombres:
        resultat *= numero
    return resultat
