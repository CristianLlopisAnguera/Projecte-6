# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 09/05/2025
#
# Versió: 1.0
#
# Descripció(programa): Biblioteca amb llibres físics i digitals usant herència

class Llibre:
    def __init__(self, titol, autor):
        self.titol = titol
        self.autor = autor

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}")

class LlibrePaper(Llibre):
    def __init__(self, titol, autor, n_pagines):
        super().__init__(titol, autor)
        self.n_pagines = n_pagines

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}, Pàgines: {self.n_pagines}")

class LlibreDigital(Llibre):
    def __init__(self, titol, autor, format):
        super().__init__(titol, autor)
        self.format = format

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}, Format: {self.format}")

paper = LlibrePaper("El Quixot", "Cervantes", 863)
digital = LlibreDigital("1984", "George Orwell", "PDF")

paper.mostrar_info()
digital.mostrar_info()