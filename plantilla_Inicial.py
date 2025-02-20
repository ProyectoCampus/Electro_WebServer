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
# Crear objetos

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
############## Rutas del proyecto ######################################################
########################################################################################

# Aquí tus rutas que llamen a las funciones de micropython que diseñes

########################################################################################
###################### Correr la APP ###################################################
########################################################################################

app.run(host="0.0.0.0", port=80)

######################################################################################