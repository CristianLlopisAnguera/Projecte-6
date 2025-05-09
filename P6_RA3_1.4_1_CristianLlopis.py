# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 09/05/2025
#
# Versió: 1.0
#
# Descripció(programa): Programa que gestiona la impressió de factures amb injecció de dependències per aconseguir baix acoblament.

class ImpressoraPDF:
    def imprimir(self, contingut):
        print(f"Imprimint PDF: {contingut}")

class Factura:
    def __init__(self, client, import_total, impressora):
        self.client = client
        self.import_total = import_total
        self.impressora = impressora  # Injectem la impressora

    def imprimir_factura(self):
        contingut = f"Factura per a {self.client}, total: {self.import_total} €"
        self.impressora.imprimir(contingut)