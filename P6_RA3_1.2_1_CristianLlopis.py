# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025 

# Versió: 1.0

# Descripció(programa): Classe Cotxe amb atributs marca, model, any i mètode per mostrar informació

class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any

    def mostrar_info(self):
        print(f"Cotxe: {self.marca} {self.model}, Any: {self.any}")

# Exemple
cotxe1 = Cotxe("Toyota", "Corolla", 2020)
cotxe1.mostrar_info()
