# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025 

# Versió: 1.0

# Descripció(programa): Classe Estudiant amb mètode dir si ha aprovat

class Estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota

    def ha_aprovat(self):
        if self.nota >= 5:
            print(f"{self.nom} ha aprovat amb {self.nota}")
        else:
            print(f"{self.nom} no ha aprovat amb {self.nota}")

# Exemple
estu = Estudiant("Laia", 6.5)
estu.ha_aprovat()
