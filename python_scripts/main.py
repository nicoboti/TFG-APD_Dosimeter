import wifi
import socket
import time
from machine import ADC, Pin

# --- 1. Conexión Wi-Fi ---
SSID = "AndroidAP"
PASSWORD = "evaalvarez"
wlan = wifi.conectar_wifi(SSID, PASSWORD)

# --- 2. Configuración ADC ---
adc = ADC(Pin(0))
adc.atten(ADC.ATTN_11DB)  # Rango 0–3.3 V

# --- 3. LEDs ---
led_verde = Pin(2, Pin.OUT)
led_rojo = Pin(3, Pin.OUT)
UMBRAL = 0.4  # V

# --- 4. HTML para el navegador ---
html = """<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Dosímetro ESP32</title>
  <script>
    async function actualizar() {
      const res = await fetch("/voltaje");
      const data = await res.json();
      document.getElementById("voltaje").innerText = data.voltaje.toFixed(3);
      document.getElementById("estado").innerText = data.estado;
    }
    setInterval(actualizar, 1000);
  </script>
</head>
<body>
  <h2>Voltaje detectado:</h2>
  <h1><span id="voltaje">0.000</span> V</h1>
  <h3>Estado de radiación: <span id="estado">N/A</span></h3>
</body>
</html>
"""

# --- 5. Servidor web ---
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print("🌐 Servidor web iniciado en:", wlan.ifconfig()[0])

# --- 6. Bucle principal ---
while True:
    cl, addr = s.accept()
    print("🌍 Cliente conectado desde", addr)
    req = cl.recv(1024).decode()

    raw = adc.read()
    voltaje = raw / 4095 * 3.3

    # Lógica de los LEDs
    if voltaje > UMBRAL:
        led_verde.on()
        led_rojo.off()
        estado = "Radiación detectada"
    else:
        led_verde.off()
        led_rojo.on()
        estado = "Sin radiación"

    if "GET /voltaje" in req:
        # Enviar solo JSON con los datos
        response = f'{{"voltaje": {voltaje:.3f}, "estado": "{estado}"}}'
        cl.send("HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n")
        cl.send(response)

    else:
        # Enviar HTML al navegador
        cl.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        cl.send(html)

    cl.close()
