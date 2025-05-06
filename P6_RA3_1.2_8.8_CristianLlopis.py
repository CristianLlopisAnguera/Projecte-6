# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025

# Versió: 1.0

# Descripció(programa): Classe Biblioteca amb afegir i mostrar llibres

class Biblioteca:
    def __init__(self):
        self.llista_llibre = []

    def afegir_llibre(self, llibre):
        self.llista_llibre.append(llibre)

    def mostrar_llibres(self):
        for llibre in self.llista_llibre:
            llibre.mostrar_info()

biblio = Biblioteca()
biblio.afegir_llibre(Llibre("1984", "George Orwell", 1949))
biblio.afegir_llibre(Llibre("El Petit Príncep", "Antoine de Saint-Exupéry", 1943))
biblio.mostrar_llibres()
