# Electro_WebServer
Se trata del uso de microcontroladores con capacidad Wifi, para el estudio de diseño WEB: [HTML](https://www.w3schools.com/html/default.asp), [CSS](https://www.w3schools.com/css/default.asp) y [JS](https://www.w3schools.com/js/default.asp) mediante la electrónica gracias a [MicroPython](https://micropython.org/) y el Framework Microdot el cuál se encuentra bien documentado inspirado en Flask pero para Microcontroladores, se ha realizado con un Microcontrolador [RP2350 + Wi-Fi b/g/n and Bluetooth via CYW43439](https://www.raspberrypi.com/products/raspberry-pi-pico-2/), luego se lo hizo compatible con [ESP8266 y ESP32](https://www.espressif.com/en/products/devkits). Por lo tanto, se pueden usar una gran variedad de microcontroladores dentro de las 2 Marcas, Raspberry Pi([RP2350 y RP2040+CYW43439](https://docs.micropython.org/en/latest/rp2/quickref.html)) o Espressif ([ESP8266](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html) y [ESP32](https://docs.micropython.org/en/latest/esp32/quickref.html)), en este último la variedad de modelos es importante: S, S2, S3, C3, C5, C6, C61.

# Estructura de Archivos:
- En el root del microcontrolador se copian las carpetas ```red ```, ```static```, ```microdot```, los archivos ```plantilla_main.py```, ```plantilla_electronica.py``` y ```plantilla_conectar,py```.
- [Microdot](https://microdot.readthedocs.io/en/latest/#) es un Framework inspirado en Flask.
- Red contiene una simple librería que se encarga de la conexión a la red Wifi. Lo único que debemos editar es el archivo ```secrets.py``` para indicar el **ssid** y el **psk** o varios de ellos si nos movemos a diferentes lugares. De usar otros ssid se debe agregar el número de cual para de credenciales vamos a usar, es útil cuando tenemos varias redes y no queremos andar cambiando los datos.
- Static contiene los archivos servidos por el servidor que corre Microdot. En ```index.html``` tenemos lo básico con un ejemplo en el body, que se borrará al iniciar un proyecto. Para manejar la estetica tenemos el ```style.css``` que readecuaremos a nuestro proyecto. Mientras que ```app.js``` se encargará de hacer ese puente entre el backend del servidor y la electrónica realizada con MicroPython en el archivo ```plantilla_electronica.py``` que es un ejemplo muy básico que también cambiaremos al realizar el proyecto, pero algo habia que mostrar!
- El archivo ```plantilla_electronica.py``` no es más que un código rudimentario transformado en Clase para que se le puedan agregar más métodos y ser reutilizado, ya que un simple on, off sirve para cualquier tipo de dispositivo de salida.
- El archivo ```plantilla_main.py``` es nuestro programa principal, el cual llama al resto de archivos y librerías, contiene un ejemplo básico de encendido y apagado, para mostrar la interacción **JS-electrónica** y una radio embebida solo para mostrar que la programación básica de cualquier curso HTML será posible. Para cualquier elemento incapaz de ser ejecutado por el microcontrolador respecto a diseño web, se pueden usar [CDNs](https://es.wikipedia.org/wiki/Red_de_distribuci%C3%B3n_de_contenidos) que nos den eso que no es capaz de bancarse el microcontrolador. Por otro lado, se muestra el código de Microdot, el cual es solo un ruteo por cada acción que necesitemos, el cual puede ser simplemente otro html para mostrar o rutas que manejan las funciones del código de MicroPython para ser usadas por JS.
- El archivo ```plantilla_conectar.py``` es para iniciar un nuevo ```proyecto.py``` desde prácticamente cero, con rutas básicas y el servidor funcionando. Es un archivo opcional con solo unas líneas menos que el de main. Tambien sirve para solo hacerte un curso de HTML, CSS, JS sin entretenerte con electrónica.

# Firmwares MicroPython:
- MicroPython RP2350 con Wifi [UF2](https://micropython.org/download/RPI_PICO_W/)
- MicroPython RP2040 con Wifi [UF2](https://micropython.org/download/RPI_PICO2_W/)
- MicroPython ESP8266 [.bin](https://micropython.org/download/ESP8266_GENERIC/) El [ESP-01](https://www.instructables.com/Getting-Started-With-the-ESP8266-ESP-01/) no es recomendado por su escaso almacenamiento, NodeMCU, LoLin es lo recomendado y por los precios mejor ESP32.
- MicroPython ESP32 WROOM (El llamado S1) [.bin](https://micropython.org/download/ESP32_GENERIC/)
- MicroPython ESP32 C3 [.bin](https://micropython.org/download/ESP32_GENERIC_C3/)
- MicroPython ESP32 C6 [.bin](https://micropython.org/download/ESP32_GENERIC_C6/)
- MicroPython ESP32 S2 [.bin](https://micropython.org/download/ESP32_GENERIC_S2/)
- MicroPython ESP32 S3 [.bin](https://micropython.org/download/ESP32_GENERIC_S3/)



