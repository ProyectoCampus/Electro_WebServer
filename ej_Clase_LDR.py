from red.miwifi import Connect
import red.secrets as secrets

########################## INTERNET ####################################################
'''Configuración WiFi'''
wifi = Connect(secrets.SECRETS['ssid'], secrets.SECRETS['psk'])

'''Mostrar si está conectado, su IPv4, su IPV6 si es compatible Subnet, Gateway, DNS'''
if wifi.show_ifv4():
    wifi.show_ipv4()
if hasattr(wifi.wlan, "ipconfig"):
    wifi.show_ipv6()
########################################################################################

########################## Electrónica #################################################
from electronica import Relay, LDR

r = Relay(pin=1)
ldr = LDR(pin=4)
########################################################################################

########################## Servidor Microdot ###########################################

from microdot.microdot import Microdot, send_file, Response
from microdot.websocket import with_websocket
import asyncio

Response.default_content_type = 'application/json'  # Configura JSON como respuesta predeterminada

app = Microdot()

@app.route('/')
async def serve_index(request):
    return send_file('static/index.html')  # Sirve la interfaz web

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
    return Response({"status": r.get_state()})  # Devuelve JSON con el estado actual

# Rutas para archivos estáticos version vieja
'''@app.route('/static/app.js')
async def serve_js(request):
    return send_file('static/app.js', content_type='application/javascript')

@app.route('/static/style.css')
async def serve_css(request):
    return send_file('static/style.css', content_type='text/css')
'''
# Rutas para archivos estaticos version optimizada, nos ahorra definir rutas nuevas en el futuro.
# Como podrian ser iconos, imagenes.
@app.route("/static/<path:path>")
async def static(request, path):
    if ".." in path:
        return Response("Not found", status=404)
    return send_file("static/" + path)

# WebSocket para el sensor LDR
@app.route('/ws')
@with_websocket
async def read_sensor(request, ws):
    while True:
        await asyncio.sleep(0.1)  # No bloquea el bucle
        await ws.send(str(ldr.get_light_percentage()))

app.run(host="0.0.0.0", port=80)
######################################################################################
