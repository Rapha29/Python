import pywifi
import time

def scan_and_display_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Use the first Wi-Fi interface

    iface.scan()  # Start scanning
    time.sleep(2)  # Wait for networks to be found

    networks = iface.scan_results()
    
    if not networks:
        print("No Wi-Fi networks found.")
    else:
        print("Available Wi-Fi networks and signal strength (RSSI):")
        for network in networks:
            print(f"SSID: {network.ssid}, RSSI: {network.signal}")

if __name__ == "__main__":
    scan_and_display_networks()
