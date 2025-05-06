# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025

# Versió: 1.0

# Descripció(programa): Classe Producte amb preu privat i controlat

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        if preu > 0:
            self.__preu = preu
        else:
            raise ValueError("El preu ha de ser positiu")

    def obtenir_preu(self):
        return self.__preu

    def modificar_preu(self, nou_preu):
        if nou_preu > 0:
            self.__preu = nou_preu
        else:
            print("Preu no vàlid")
