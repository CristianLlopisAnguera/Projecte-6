# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 09/05/2025
#
# Versió: 1.0
#
# Descripció(programa): Vehicles amb herència i mètodes arrencar i tocar_claxon

class Vehicle:
    def __init__(self, marca):
        self.marca = marca

    def arrencar(self):
        print(f"{self.marca} arrencat.")

class Cotxe(Vehicle):
    def tocar_claxon(self):
        print("Pip pip!")

cotxe = Cotxe("Toyota")
cotxe.arrencar()
cotxe.tocar_claxon()