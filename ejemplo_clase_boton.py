from electronica import Button
import time

button = Button(pin=3, pull_up=False)  # Botón en el pin 3 con pull-down
last_state = None  # Estado anterior del botón (inicialmente indefinido)

while True:
    current_state = button.is_pressed()  # Lee el estado actual del botón

    if current_state != last_state:  # Solo imprime si el estado cambió
        if current_state:
            print(f"Botón presionado {button.button.value()}")
        else:
            print(f"Botón no presionado {button.button.value()}")
    
    last_state = current_state  # Actualiza el estado anterior
    time.sleep(0.05)  # Pequeño retardo para evitar rebotes

