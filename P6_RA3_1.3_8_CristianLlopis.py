# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025

# Versió: 1.0

# Descripció(programa): Classe Alumne amb edat no negativa

class Alumne:
    def __init__(self, nom, edat):
        self.nom = nom
        self.__edat = 0
        self.edat = edat

    @property
    def edat(self):
        return self.__edat

    @edat.setter
    def edat(self, valor):
        if valor >= 0:
            self.__edat = valor
        else:
            print("Edat no pot ser negativa")
