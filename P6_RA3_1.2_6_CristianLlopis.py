# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025 

# Versió: 1.0

# Descripció(programa): Classe CompteBancari amb ingressar, retirar i veure saldo

class CompteBancari:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def ingressar(self, quantitat):
        self.saldo += quantitat

    def retirar(self, quantitat):
        if quantitat <= self.saldo:
            self.saldo -= quantitat
        else:
            print("No tens prou saldo!")

    def veure_saldo(self):
        print(f"Saldo actual: {self.saldo}€")

# Exemple
compte = CompteBancari(100)
compte.ingressar(50)
compte.retirar(30)
compte.veure_saldo()
