########################################################################################
########################## INTERNET ####################################################
########################################################################################

from red.miwifi import Connect
import red.secrets as secrets

wifi = Connect(secrets.SECRETS['ssid'], secrets.SECRETS['psk'])

'''Mostrar si está conectado, su IPv4, su IPV6 si es compatible Subnet, Gateway, DNS'''
if not wifi.show_ifv4():
    wifi.show_ipv4()
if hasattr(wifi.wlan, "ipconfig"):
    wifi.show_ipv6()


########################################################################################
########################## Electronica #################################################
########################################################################################

from electronica import Relay,LDR, Button

r = Relay(pin=1) # para dispositivos de salida

button_pull_up = Button(pin=3, pull_up=True) # para dispositivos de entrada pull_up
button_pull_down = Button(pin=5, pull_up=False) # para dispositivos de entrada pull_down

ldr = LDR(pin=4) # para dispositivos ADC


########################################################################################
########################## Conexión con Server Microdot ################################
########################################################################################

from microdot.microdot import Microdot, send_file, Response
from microdot.websocket import with_websocket # Cuando usas websocket
import asyncio # Necesario para Websocket
import json

Response.default_content_type = 'application/json'  # Configura JSON como respuesta predeterminada

app = Microdot()


########################################################################################
################## Server HTML, CSS, JS ################################################
########################################################################################

@app.route('/')
async def serve_index(request):
    return send_file('static/index.html')  # Sirve la interfaz web

# Rutas para archivos estaticos
@app.route("/static/<path:path>")
async def static(request, path):
    if ".." in path:
        return Response("Not found", status=404)
    return send_file("static/" + path)


########################################################################################
############## Relay (Ejemplo Relay/LED) ###############################################
########################################################################################

@app.route('/on')
async def turn_on(request):
    r.on()  # Enciende el relé
    return Response({"status": "on"})  # Devuelve JSON con el estado

@app.route('/off')
async def turn_off(request):
    r.off()  # Apaga el relé
    return Response({"status": "off"})  # Devuelve JSON con el estado

@app.route('/status')
async def get_status(request):
    return Response({"status": r.get_state()})


########################################################################################
############## Button (Ejemplo Boton)###################################################
########################################################################################

# WebSocket para los botones
@app.route('/ws/buttons')
@with_websocket
async def send_buttons_status(request, ws):
    while True:
        # Leer el estado de los botones
        pullup_state = button_pull_up.is_pressed()
        pulldown_state = button_pull_down.is_pressed()

        # Crear un objeto con el estado de los botones
        data = {
            "button_pull_up": pullup_state,
            "button_pull_down": pulldown_state
        }
        
        # Enviar el estado de los botones a través del WebSocket
        await ws.send(json.dumps(data))

        # Esperar un poco antes de la siguiente lectura
        await asyncio.sleep(0.1)


########################################################################################
###################### LDR (Ejemplo LDR)################################################
########################################################################################

@app.route('/ws/ldr')
@with_websocket
async def read_sensor(request, ws):
    while True:
        #Leer el porcentaje de luz
        light_percentage = ldr.get_light_percentage()
        await ws.send(str(light_percentage)) # Enviar datos del sensor
        await asyncio.sleep(0.1)  # No bloquea el bucle
        

########################################################################################
###################### Correr la APP ###################################################
########################################################################################

app.run(host="0.0.0.0", port=80)

######################################################################################