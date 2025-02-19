from machine import Pin

relayPin = Pin(1, Pin.OUT)  # Pin global (opcional)

class Relay():
    def __init__(self, pin):
        self.relayPin = Pin(pin, Pin.OUT)  # Inicializa un pin para la instancia

    def on(self):
        self.relayPin.value(0)  # Enciende el relé

    def off(self):
        self.relayPin.value(1)  # Apaga el relé