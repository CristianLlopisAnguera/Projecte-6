# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025 

# Versió: 1.0

# Descripció(programa): Classe Rectangle amb mètodes area i perimetre

class Rectangle:
    def __init__(self, amplada, alcada):
        self.amplada = amplada
        self.alcada = alcada

    def area(self):
        return self.amplada * self.alcada

    def perimetre(self):
        return 2 * (self.amplada + self.alcada)

# Exemple
rect = Rectangle(4, 5)
print("Àrea:", rect.area())
print("Perímetre:", rect.perimetre())
