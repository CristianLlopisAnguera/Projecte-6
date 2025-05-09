# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 09/05/2025
#
# Versió: 1.0
#
# Descripció(programa): Transport amb polimorfisme i simulació de moviment

class Vehicle:
    def moure(self):
        pass

class Cotxe(Vehicle):
    def moure(self):
        print("El cotxe està conduint per la carretera.")

class Bicicleta(Vehicle):
    def moure(self):
        print("La bicicleta pedaleja pel carril bici.")

class Barca(Vehicle):
    def moure(self):
        print("La barca navega pel riu.")

def simular_moviment(vehicles):
    for vehicle in vehicles:
        vehicle.moure()

vehicles = [Cotxe(), Bicicleta(), Barca()]
simular_moviment(vehicles)