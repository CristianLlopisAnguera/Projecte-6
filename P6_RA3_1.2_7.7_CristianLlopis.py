# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025

# Versió: 1.0

# Descripció(programa): Classe Gos que sobreescriu fer_soroll()

class Gos(Animal):
    def fer_soroll(self):
        print(f"{self.nom} diu: Bup bup!")

g = Gos("Rex", "gos")
g.fer_soroll()
