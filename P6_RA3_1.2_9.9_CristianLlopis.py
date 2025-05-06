# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025

# Versió: 1.0

# Descripció(programa): Mostrar cercles amb àrea superior a 50

cercles = [
    Cercle(3),
    Cercle(5),
    Cercle(8)
]

for i, cercle in enumerate(cercles, 1):
    if cercle.area() > 50:
        print(f"Cercle {i} amb radi {cercle.radi} té àrea {cercle.area():.2f} (>50)")
