# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 09/05/2025
#
# Versió: 1.0
#
# Descripció(programa): Classe Comanda amb baix acoblament que rep el notificador com a dependència.

class Comanda:
    def __init__(self, client, notificador):
        self.client = client
        self.notificador = notificador

    def confirmar(self):
        print(f"Comanda confirmada per {self.client}")
        self.notificador.enviar(f"Hola {self.client}, la teva comanda ha estat confirmada.")
