from red.miwifi import Connect
import red.secrets as secrets

########################## INTERNET ###################################################
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
from microdot.microdot import Microdot, send_fileResponse

Response.default_content_type = 'application/json'  # Configura JSON como respuesta predeterminada

app = Microdot()

@app.route('/')
async def serve_index(request):
    return send_file('/static/index.html')  # Sirve la interfaz web

# Ruta para servir el archivo app.js
@app.route('/static/app.js')
async def serve_js(request):
    return send_file('static/app.js', content_type='application/javascript')

# Ruta para servir el archivo style.css
@app.route('/static/style.css')
async def serve_css(request):
    return send_file('static/style.css', content_type='text/css')

# Otras funciones: #

####################
app.run(host="0.0.0.0", port=80)
########################################################################################