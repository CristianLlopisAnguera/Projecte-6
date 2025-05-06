# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025 

# Versió: 1.0

# Descripció(programa): Classe Producte amb mètode aplicar descompte

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.preu = preu

    def aplicar_descompte(self, percentatge):
        self.preu -= self.preu * (percentatge / 100)

# Exemple
prod = Producte("Portàtil", 1000)
prod.aplicar_descompte(10)
print(f"Preu amb descompte: {prod.preu}€")
