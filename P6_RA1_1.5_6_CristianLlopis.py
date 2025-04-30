# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 29/04/2025

# Versió: 1.0

# Descripció(programa): Mostra la primera i l'última lletra d'una cadena.

text = input("Introdueix una cadena: ")
if len(text) > 0:
    print("Primera lletra:", text[0])
    print("Última lletra:", text[-1])
else:
    print("Has d'introduir almenys una lletra.")