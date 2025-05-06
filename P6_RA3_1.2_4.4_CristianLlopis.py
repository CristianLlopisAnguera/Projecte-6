# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025

# Versió: 1.0

# Descripció(programa): Compte bancari amb ingrés i retirades

compte = CompteBancari(100)
compte.ingressar(50)
compte.retirar(30)
compte.retirar(200)  # retirada superior al saldo
compte.veure_saldo()
