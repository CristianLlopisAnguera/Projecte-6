# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 09/05/2025
#
# Versió: 1.0
#
# Descripció(programa): Empleats amb polimorfisme i càlcul de sous

class Empleat:
    def calcular_sou(self):
        pass

class Fixe(Empleat):
    def calcular_sou(self):
        return 2000

class Autonom(Empleat):
    def calcular_sou(self):
        return 1500

def mostrar_sous(llista_empleats):
    for empleat in llista_empleats:
        print(f"Sou: {empleat.calcular_sou()}€")

empleats = [Fixe(), Autonom(), Fixe()]

mostrar_sous(empleats)