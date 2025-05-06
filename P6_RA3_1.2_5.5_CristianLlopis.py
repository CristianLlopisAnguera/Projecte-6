# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025

# Versió: 1.0

# Descripció(programa): Aplicar descompte del 10% a una llista de productes

def aplicar_descompte_tots(productes):
    for prod in productes:
        prod.aplicar_descompte(10)
        print(f"{prod.nom}: {prod.preu:.2f}€ després del descompte")

productes = [
    Producte("Portàtil", 1200),
    Producte("Tablet", 600),
    Producte("Smartphone", 800)
]

aplicar_descompte_tots(productes)
