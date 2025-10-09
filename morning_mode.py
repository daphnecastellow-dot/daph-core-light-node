# morning_mode.py
# Gradual sunrise-style wake-up lighting
# Author: Daphne Castellow
# License: MIT

import time, machine
from neopixel import NeoPixel

# --- Setup ---
pin = machine.Pin(4, machine.Pin.OUT)
np = NeoPixel(pin, 1)

def set_color(r, g, b, brightness=0.5):
    np[0] = (int(r * brightness), int(g * brightness), int(b * brightness))
    np.write()

def sunrise_fade(minutes=15):
    """
    Simulate sunrise by brightening from dark red to soft white.
    Default runtime: 15 minutes, gentle 5 s steps.
    """
    steps = int(minutes * 12)
    for i in range(steps + 1):
        # color ramp: red → orange → yellow → white
        r = min(255, int(120 + (i / steps) * 135))
        g = min(255, int((i / steps) * 180))
        b = int((i / steps) * 120)
        brightness = min(1.0, 0.1 + (i / steps) * 0.9)
        set_color(r, g, b, brightness)
        time.sleep(5)
