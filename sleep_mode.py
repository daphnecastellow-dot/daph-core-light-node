# sleep_mode.py
# Gentle warm fade for bedtime
# Author: Daphne Castellow
# License: MIT

import time, machine
from neopixel import NeoPixel

# --- Setup ---
pin = machine.Pin(4, machine.Pin.OUT)
np = NeoPixel(pin, 1)

def set_color(r, g, b, brightness=0.3):
    """Set NeoPixel color with adjustable brightness."""
    np[0] = (int(r * brightness), int(g * brightness), int(b * brightness))
    np.write()

def sleep_fade(color=(255, 160, 80), minutes=20):
    """
    Warm amber light that fades slowly to darkness.
    Default runtime: 20 minutes.
    Each step dims every 5 seconds.
    """
    steps = int(minutes * 12)  # 12 steps per minute
    for i in range(steps, -1, -1):
        level = i / steps
        set_color(*color, brightness=0.3 * level)
        time.sleep(5)
    # turn off completely
    set_color(0, 0, 0, 0)
