# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025

# Versió: 1.0

# Descripció(programa): Classe Sensor amb valor limitat

class Sensor:
    def __init__(self, valor=0):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, nou_valor):
        if 0 <= nou_valor <= 100:
            self.__valor = nou_valor
        else:
            print("Valor fora de rang (0-100)")
