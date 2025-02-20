'''
Conexión PULL_UP usando resistencia interna:
            button = Button(pin=3) # El parametro pull_up es innecesario, esta por defecto en la clase
                    pin --> boton --> GND

Conexión PULL_DOWN:
            button = Button(pin=4, pull_up=False) para pull_down conectar resistencia externa de 10k
                    3v3 --> boton --> Pin
                                  |--> resistencia --> GND

'''
from electronica import Button
import time

# Botón con pull-up interno (conexión entre pin y GND)
button_pull_up = Button(pin=3, pull_up=True)  # Botón en el pin 3 con pull-up

# Botón con resistencia externa pull-down (conexión entre pin y 3.3V)
button_pull_down = Button(pin=4, pull_up=False)  # Botón en el pin 5 con pull-down

# Estado anterior de ambos botones
last_state_pull_up = None
last_state_pull_down = None

while True:
    # Lee el estado de cada botón
    current_state_pull_up = button_pull_up.is_pressed()
    current_state_pull_down = button_pull_down.is_pressed()

    # Si el estado del botón con pull-up ha cambiado, imprime el estado
    if current_state_pull_up != last_state_pull_up:
        if current_state_pull_up:
            print(f"Botón con pull-up presionado {button_pull_up.button.value()}")
        else:
            print(f"Botón con pull-up no presionado {button_pull_up.button.value()}")
    
    # Si el estado del botón con pull-down ha cambiado, imprime el estado
    if current_state_pull_down != last_state_pull_down:
        if current_state_pull_down:
            print(f"Botón con pull-down presionado {button_pull_down.button.value()}")
        else:
            print(f"Botón con pull-down no presionado {button_pull_down.button.value()}")
    
    # Actualiza el estado anterior de ambos botones
    last_state_pull_up = current_state_pull_up
    last_state_pull_down = current_state_pull_down

    time.sleep(0.05)  # Pequeño retardo para evitar rebotes
