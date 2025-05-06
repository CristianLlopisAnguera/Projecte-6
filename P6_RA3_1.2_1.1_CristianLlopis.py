# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 06/05/2025

# Versió: 1.0

# Descripció(programa): Crear dos cotxes i mostrar informació

from cotxe import Cotxe  # Si la classe està en un mòdul, sinó elimina aquesta línia

cotxe1 = Cotxe("Ford", "Focus", 2018)
cotxe2 = Cotxe("BMW", "X3", 2021)

cotxe1.mostrar_info()
cotxe2.mostrar_info()
