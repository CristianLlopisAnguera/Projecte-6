# Administració de sistemes informatics en Xarxa
# Autor: Cristian Llopis Anguera
# Data: 09/05/2025
#
# Versió: 1.0
#
# Descripció(programa): Missatgeria amb polimorfisme i enviament de missatges

class Missatger:
    def enviar(self, missatge):
        pass

class Email(Missatger):
    def enviar(self, missatge):
        print(f"Enviant Email: {missatge}")

class SMS(Missatger):
    def enviar(self, missatge):
        print(f"Enviant SMS: {missatge}")

class WhatsApp(Missatger):
    def enviar(self, missatge):
        print(f"Enviant WhatsApp: {missatge}")

def enviar_missatges(missatgers, missatge):
    for missatger in missatgers:
        missatger.enviar(missatge)

missatgers = [Email(), SMS(), WhatsApp()]
enviar_missatges(missatgers, "Hola, aquest és el missatge!")