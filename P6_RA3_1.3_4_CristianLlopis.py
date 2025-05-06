# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025

# Versió: 1.0

# Descripció(programa): Classe Usuari amb contrasenya privada

class Usuari:
    def __init__(self, contrasenya):
        if len(contrasenya) >= 8:
            self.__contrasenya = contrasenya
        else:
            raise ValueError("Contrasenya massa curta")

    def canviar_contrasenya(self, nova):
        if len(nova) >= 8:
            self.__contrasenya = nova
            print("Contrasenya canviada")
        else:
            print("La nova contrasenya és massa curta")

    def verificar_contrasenya(self, clau):
        return self.__contrasenya == clau
