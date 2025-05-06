# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025

# Versió: 1.0

# Descripció(programa): Classe Punt amb mètode per calcular distància a un altre punt

import math

class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, altre_punt):
        return math.sqrt((self.x - altre_punt.x) ** 2 + (self.y - altre_punt.y) ** 2)

# Exemple
p1 = Punt(0, 0)
p2 = Punt(3, 4)
print("Distància:", p1.distancia(p2))
