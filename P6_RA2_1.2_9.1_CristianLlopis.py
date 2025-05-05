# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025 

# Versió: 1.0

# Descripció(programa): Determina l'estat d'una persona segons l'edat

def estat_persona(edat):
    if edat < 18:
        estat = "Menor d'edat"
        descripcio = "No és adult encara."
    elif edat < 65:
        estat = "Adult"
        descripcio = "Persona en edat laboral."
    else:
        estat = "Jubilat"
        descripcio = "Persona retirada."
    return estat, descripcio

for edat in [12, 25, 70]:
    estat, descripcio = estat_persona(edat)
    print(f"Edat: {edat} -> {estat} ({descripcio})")
