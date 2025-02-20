from machine import Pin, ADC
import sys

class Relay():
    '''Uso:
            relay = Relay(pin=1)
            Métodos:
                    relay.on()
                    relay.off()
                    get_state()
    '''
    def __init__(self, pin):
        self.relayPin = Pin(pin, Pin.OUT)  # Inicializa un pin para la instancia
    
    def on(self):
        self.relayPin.value(0)  # Enciende el relé

    def off(self):
        self.relayPin.value(1)  # Apaga el relé
    
    def get_state(self):
        return "on" if self.relayPin.value() == 0 else "off"

class Button():
    '''Uso:
            Conexión PULL_DOWN:
            button = Button(pin=3, pull_up=False) para pull_down conectar resistencia externa de 10k
                    3v3 --> boton --> Pin
                                  |--> resistencia --> GND
            Conexión PULL_UP usando resistencia interna:
            button = Button(pin=3)
                    pin --> boton --> GND
            Métodos:
                    button.is_pressed()
                    button.wait_for_press()
    '''
    def __init__(self, pin, pull_up=True):
        self.platform = sys.platform
        self.pull_up = pull_up
        self.button = Pin(pin, Pin.IN, Pin.PULL_UP if pull_up else Pin.PULL_DOWN)
    
    def is_pressed(self):
        if "esp32" in self.platform:
            if self.pull_up:
                return self.button.value() == 0  # Con PULL_UP, 0 indica que está presionado
            else:
                return self.button.value() == 1  # Con PULL_DOWN, 1 indica que está presionado
        elif "rp2" in self.platform:
            if self.pull_up:
                return self.button.value() == 1  # En RP2040, 1 indica que está presionado con PULL_UP
            else:
                return self.button.value() == 0  # Con PULL_DOWN, 0 indica que está presionado
        return False
    
    def wait_for_press(self):
        while not self.is_pressed():
            pass

class LDR():
    '''Uso:
            ldr = LDR(pin=32)
            Métodos:
                    ldr.get_raw_value()
                    ldr.get_light_percentage()
    '''
    def __init__(self, pin):
        self.adc_pin = ADC(Pin(pin))
        
    def get_raw_value(self):
        return self.adc_pin.read_u16()
    
    def get_light_percentage(self):
        return round((self.get_raw_value()/65535*100),2)