# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025

# Versió: 1.0

# Descripció(programa): Mostrar persones amb més de 30 anys

def mostrar_persones_majors(persones):
    for persona in persones:
        if persona.edat > 30:
            print(f"{persona.nom}, {persona.edat} anys")

persones = [
    Persona("Joan", 28),
    Persona("Anna", 35),
    Persona("Pere", 40)
]

mostrar_persones_majors(persones)
