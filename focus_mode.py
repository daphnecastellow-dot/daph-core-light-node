# focus_mode.py
# Steady cool-blue light for concentration
# Author: Daphne Castellow
# License: MIT

import time, machine
from neopixel import NeoPixel

# --- Setup ---
pin = machine.Pin(4, machine.Pin.OUT)
np = NeoPixel(pin, 1)

def set_color(r, g, b, brightness=0.6):
    """Set NeoPixel color with adjustable brightness."""
    np[0] = (int(r * brightness), int(g * brightness), int(b * brightness))
    np.write()

def focus_light(color=(135, 206, 250), duration_minutes=None):
    """
    Hold a steady cool-blue light to support concentration or study.
    If duration_minutes is set, the light will stay on for that period then fade out.
    """
    set_color(*color, brightness=0.6)
    if duration_minutes is None:
        # Indefinite focus mode
        while True:
            time.sleep(60)
    else:
        # Timed session with gentle fade-out at the end
        total_seconds = int(duration_minutes * 60)
        time.sleep(total_seconds)
        # Quick fade-out sequence
        for i in range(100, -1, -5):
            set_color(*color, brightness=0.6 * i/100)
            time.sleep(0.1)
        set_color(0, 0, 0, 0)
