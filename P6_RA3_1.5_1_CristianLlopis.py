# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 09/05/2025
#
# Versió: 1.0
#
# Descripció(programa): Animals amb herència i mètode parlar()

class Animal:
    def parlar(self):
        pass

class Gos(Animal):
    def parlar(self):
        print("Bup bup!")

class Gat(Animal):
    def parlar(self):
        print("Miau!")

gos = Gos()
gat = Gat()

gos.parlar()
gat.parlar()