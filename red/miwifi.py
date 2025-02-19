import time, network, sys

class Connect():
    def __init__(self, ssid, psk):
        # Crear y activar la interfaz Wi-Fi
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.connect(ssid, psk)  # Llamar al método connect desde el constructor
        self.prefer_ifv4 = hasattr(self.wlan, "ifconfig")
        
    '''Uso connect(ssid,psk)'''
    def connect(self, ssid, psk):
        '''conectar a una red Wi-Fi'''
        if sys.platform == "rp2":
            import rp2
            rp2.country("AR")
            
        self.wlan.connect(ssid,psk)
        max_wait = 30
        while max_wait > 0:
            if self.wlan.status() == network.STAT_GOT_IP:
                print("Conectado")
                return # Se sale del bucle al ya estar conectado
            elif self.wlan.status() < 0:
                print("Error al intentar conectarse")
                raise RuntimeError("Conexión fallida, revisa ssi y psk sean correctos")
            max_wait -= 1
            print("Esperando conectarse a WiFi...")
            time.sleep(1)
        raise RuntimeError("No se estabeció conexión tras 30 segundos, revisa las credenciales y la distancia con la red.")

    '''Uso show_ifv4()'''
    def show_ifv4(self): 
        '''Muestra la configuración IPv4 (prioritaria si está disponible)'''
        if not hasattr(self.wlan, "ifconfig"):
            print("ifv4 no disponible, intentando con ipv4...")
            self.show_ipv4()
            return False

        print("\n\tInformación de Red (ifv4):\n")
        ip, subnet, gateway, dns = self.wlan.ifconfig()
        print(f"\t\tConectado: {self.wlan.isconnected()} \n\t\tIP: {ip} \n\t\tSubnet: {subnet} \n\t\tGateway: {gateway} \n\t\tDNS: {dns}")
        return True

    def show_ipv4(self): 
        '''Muestra la configuración IPv4 solo si ifv4 no está disponible'''
        if self.prefer_ifv4:
            print("IPv4 omitido porque ifv4 está disponible.")
            return

        if not hasattr(self.wlan, "ipconfig"):
            print("Error: No se puede obtener la configuración de red.")
            return

        print("\n\tInformación de Red (ipv4):\n")
        ip, subnet = self.wlan.ipconfig('addr4')
        gateway = self.wlan.ipconfig('gw4')
        print(f"\t\tConectado: {self.wlan.isconnected()} \n\t\tIP: {ip} \n\t\tSubnet: {subnet} \n\t\tGateway: {gateway}")

    '''Uso show_ipv6()'''
    def show_ipv6(self):
        '''Muestra la configuración IPv6 (si está disponible)'''
        if not hasattr(self.wlan, "ipconfig"):
            print("\nIPv6 no soportado en este dispositivo.")
            return
        try:
            valid_keys = dir(self.wlan.ipconfig)
            if 'addr6' not in valid_keys:
                print("\nIPv6 no soportado en esta plataforma.")
                return
            
            print("\n\tInformación IPv6:\n")
            ipv6, subnetv6 = self.wlan.ipconfig('addr6')
            print(f"\t\tConectado: {self.wlan.isconnected()} \n\t\tIPv6: {ipv6} \n\t\tSubnet: {subnetv6}")
        except (OSError, ValueError) as e:
            print(f"\nError obteniendo IPv6: {e}")