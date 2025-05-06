# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025 

# Versió: 1.0

# Descripció(programa): Classe Cercle amb mètodes àrea i perímetre

import math

class Cercle:
    def __init__(self, radi):
        self.radi = radi

    def area(self):
        return math.pi * self.radi ** 2

    def perimetre(self):
        return 2 * math.pi * self.radi

# Exemple
cercle = Cercle(3)
print("Àrea:", cercle.area())
print("Perímetre:", cercle.perimetre())
