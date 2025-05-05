# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025

# Versió: 1.0

# Descripció(programa): Mòdul amb validació de correu i telèfon

import re

def es_email_valid(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def es_telefon_valid(telefon):
    return re.match(r"^\d{9}$", telefon) is not None
