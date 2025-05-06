# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025

# Versió: 1.0

# Descripció(programa): Compte bancari amb saldo privat

class CompteBancari:
    def __init__(self, saldo=0):
        self.__saldo = saldo

    def ingressar(self, quantitat):
        self.__saldo += quantitat

    def retirar(self, quantitat):
        if quantitat <= self.__saldo:
            self.__saldo -= quantitat
        else:
            print("Fons insuficients")

    def consultar_saldo(self):
        return self.__saldo
