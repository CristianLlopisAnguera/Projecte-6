# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025

# Versió: 1.0

# Descripció(programa): Classe Estudiant amb atribut protegit _nota

class Estudiant:
    def __init__(self, nom, nota=0):
        self.nom = nom
        self._nota = nota

    def llegir_nota(self):
        return self._nota

    def modificar_nota(self, nova_nota):
        if 0 <= nova_nota <= 10:
            self._nota = nova_nota
        else:
            print("Nota no vàlida")
