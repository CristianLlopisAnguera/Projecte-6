# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025

# Versió: 1.0

# Descripció(programa): Crear 3 rectangles i mostrar àrees

rectangles = [
    Rectangle(4, 5),
    Rectangle(6, 7),
    Rectangle(2, 3)
]

for i, rect in enumerate(rectangles, 1):
    print(f"Àrea del rectangle {i}: {rect.area()}")
