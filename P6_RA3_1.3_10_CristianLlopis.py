# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025

# Versió: 1.0

# Descripció(programa): Classe CompteUsuari amb email validat

class CompteUsuari:
    def __init__(self, email):
        self.__email = None
        self.email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        if "@" in valor and "." in valor:
            self.__email = valor
        else:
            print("Email no vàlid")
