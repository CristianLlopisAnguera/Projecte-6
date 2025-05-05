# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025

# Versió: 1.0

# Descripció(programa): Calcula àrees amb dades de l'usuari

import geometria

c = float(input("Costat del quadrat: "))
print(f"Àrea quadrat: {geometria.area_quadrat(c)}")

r = float(input("Radi del cercle: "))
print(f"Àrea cercle: {geometria.area_cercle(r)}")

b = float(input("Base del rectangle: "))
h = float(input("Altura del rectangle: "))
print(f"Àrea rectangle: {geometria.area_rectangle(b, h)}")
