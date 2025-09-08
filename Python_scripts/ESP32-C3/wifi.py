import network
import time

def conectar_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    print("Conectando a Wi-Fi...")
    intento = 0
    while not wlan.isconnected() and intento < 20:
        time.sleep(0.5)
        print(".", end="")
        intento += 1

    if wlan.isconnected():
        print("\n✅ Conectado a Wi-Fi:", wlan.ifconfig())
        return wlan
    else:
        print("\n❌ No se pudo conectar al Wi-Fi.")
        return None
