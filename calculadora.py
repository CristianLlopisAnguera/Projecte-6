# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025

# Versió: 1.0

# Descripció(programa): Mòdul amb funcions de càlcul bàsic

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacio(a, b):
    return a * b

def divisio(a, b):
    if b != 0:
        return a / b
    else:
        return "No es pot dividir per zero"