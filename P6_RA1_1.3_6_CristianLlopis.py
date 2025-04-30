# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 29/04/2025

# Versió: 1.0

# Descripció(programa): Mostra els primers 10 termes de la seqüència de Fibonacci.

a, b = 0, 1

print("Primers 10 termes de la seqüència de Fibonacci:")

for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b
