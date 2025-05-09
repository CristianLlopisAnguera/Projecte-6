# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 09/05/2025
#
# Versió: 1.0
#
# Descripció(programa): Sons d’animals amb polimorfisme i funció reproduir_soroll

class Animal:
    def fer_soroll(self):
        pass

class Gat(Animal):
    def fer_soroll(self):
        return "Miau"

class Vaca(Animal):
    def fer_soroll(self):
        return "Muuu"

def reproduir_soroll(animal):
    print(animal.fer_soroll())

gat = Gat()
vaca = Vaca()

reproduir_soroll(gat)
reproduir_soroll(vaca)