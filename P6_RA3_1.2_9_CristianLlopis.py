# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025 

# Versió: 1.0

# Descripció(programa): Classe Llibre amb mètode mostrar_info()

class Llibre:
    def __init__(self, titol, autor, any):
        self.titol = titol
        self.autor = autor
        self.any = any

    def mostrar_info(self):
        print(f"'{self.titol}' de {self.autor} ({self.any})")

# Exemple
llibre = Llibre("1984", "George Orwell", 1949)
llibre.mostrar_info()
