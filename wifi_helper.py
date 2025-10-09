# wifi_helper.py
# Read-only Wi-Fi signal strength helper for Daph Core Light Node
# Author: Daphne Castellow
# License: MIT

import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

def get_strength():
    """Return the RSSI (dBm) of the connected Wi-Fi network or None."""
    if not wlan.isconnected():
        return None
    current = wlan.config('essid')
    try:
        nets = wlan.scan()
        for n in nets:
            if n[0].decode() == current:
                return n[3]
    except Exception as e:
        print("Wi-Fi scan error:", e)
    return None

def strength_to_brightness(rssi):
    """Convert RSSI (-90 to -30 dBm) into brightness 0.1–1.0."""
    if rssi is None:
        return 0.1
    brightness = (rssi + 90) / 60
    return max(0.1, min(1.0, brightness))
