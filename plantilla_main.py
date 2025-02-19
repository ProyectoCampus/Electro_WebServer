from red.miwifi import Connect
import red.secrets as secrets

########################## INTERNET ####################################################
'''Configuracion Wifi'''
wifi = Connect(secrets.SECRETS['ssid'], secrets.SECRETS['psk'])

'''Mostrar si está conectado, su IPv4, su IPV6 si es compatible Subnet, Gateway, DNS'''
if not wifi.show_ifv4():
    wifi.show_ipv4()
if hasattr(wifi.wlan, "ipconfig"):
    wifi.show_ipv6()
########################################################################################

########################## Electronica #################################################
from electronica import Relay
pin = 1
r = Relay(pin)
########################################################################################

########################## Con server Microdot #########################################

from microdot.microdot import Microdot, send_file, Response

Response.default_content_type = 'application/json'  # Configura JSON como respuesta predeterminada

app = Microdot()

@app.route('/')
async def serve_index(request):
    return send_file('/static/index.html')  # Sirve la interfaz web

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
    estado = "on" if r.relayPin.value() == 0 else "off"  # Corrige la lectura del estado
    return Response({"status": estado})  # Devuelve JSON con el estado actual

# Ruta para servir el archivo app.js
@app.route('/static/app.js')
async def serve_js(request):
    return send_file('static/app.js', content_type='application/javascript')

# Ruta para servir el archivo style.css
@app.route('/static/style.css')
async def serve_css(request):
    return send_file('static/style.css', content_type='text/css')

app.run(host="0.0.0.0", port=80)
######################################################################################
