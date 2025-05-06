# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025

# Versió: 1.0

# Descripció(programa): Classe Rellotge amb hores entre 0 i 23

class Rellotge:
    def __init__(self, hores=0):
        self.__hores = hores

    @property
    def hores(self):
        return self.__hores

    @hores.setter
    def hores(self, valor):
        if 0 <= valor <= 23:
            self.__hores = valor
        else:
            print("Hora fora de rang (0-23)")

    def mostrar(self):
        return f"{self.__hores:02d}:00"
