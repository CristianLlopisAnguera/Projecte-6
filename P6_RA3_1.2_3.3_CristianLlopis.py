# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025

# Versió: 1.0

# Descripció(programa): Mostrar estudiants aprovats

estudiants = [
    Estudiant("Joan", 4),
    Estudiant("Laia", 7),
    Estudiant("Pere", 5),
    Estudiant("Maria", 3)
]

for e in estudiants:
    if e.nota >= 5:
        print(f"{e.nom} ha aprovat amb {e.nota}")
