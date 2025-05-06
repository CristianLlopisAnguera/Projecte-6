# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025

# Versió: 1.0

# Descripció(programa): Classe Termostat amb getter i setter

class Termostat:
    def __init__(self, temperatura=20):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if 10 <= valor <= 30:
            self.__temperatura = valor
        else:
            print("Temperatura fora de rang (10-30)")
