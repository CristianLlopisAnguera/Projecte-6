# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 25/04/2025

# Versió: 1.0

# Descripció(programa):

numero1 = float(input("Introdueix el primer número: "))
numero2 = float(input("Introdueix el segon número: "))

print("Selecciona l'operació:")
print("1. Suma (+)")
print("2. Resta (-)")
print("3. Multiplicació (*)")
print("4. Divisió (/)")

opcio = input("Introdueix el número de l'operació: ")

if opcio == '1':
  resultat = numero1 + numero2
  print("La suma és:", resultat)
if opcio == '2':
  resultat = numero1 - numero2
  print("La resta és:", resultat)
if opcio == '3':
  resultat = numero1 * numero2
  print("La multiplicació és:", resultat)
if opcio == '4':
  if numero2 == 0:
    print("Error! No es pot dividir per zero.")
  else:
    resultat = numero1 / numero2
    print("La divisió és:", resultat)
if opcio != '1' and opcio != '2' and opcio != '3' and opcio != '4':
  print("Opció no vàlida.")