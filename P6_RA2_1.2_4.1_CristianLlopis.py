# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025 

# Versió: 1.0

# Descripció(programa): Comprova si els nombres d'una llista són parells

def es_parell(numero):
    return numero % 2 == 0

for numero in [1, 2, 3, 4, 5, 6]:
    print(f"El número {numero} és parell: {es_parell(numero)}")
