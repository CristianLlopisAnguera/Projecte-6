# Administració de sistemes informatics en Xarxa 
# Autor: Cristian Llopis Anguera
# Data: 04/05/2025 

# Versió: 1.0

# Descripció(programa): Llegeix un fitxer assegurant que sempre es tanqui, fins i tot amb errors

fitxer = None
try:
    fitxer = open('missatge.txt', 'r', encoding='utf-8')
    for linia in fitxer:
        if "error" in linia:
            raise Exception("S'ha trobat un error en el contingut!")
        print(linia.strip())
except Exception as e:
    print(f"Ha ocorregut un error: {e}")
finally:
    if fitxer:
        fitxer.close()
        print("El fitxer s'ha tancat correctament.")
