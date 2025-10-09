# alert_mode.py
# Short bright pulses for gentle notifications or reminders
# Author: Daphne Castellow
# License: MIT

import time, machine
from neopixel import NeoPixel

# --- Setup ---
pin = machine.Pin(4, machine.Pin.OUT)
np = NeoPixel(pin, 1)

def set_color(r, g, b, brightness=1.0):
    """Set NeoPixel color at full brightness for alerts."""
    np[0] = (int(r * brightness), int(g * brightness), int(b * brightness))
    np.write()

def pulse_alert(color=(255, 80, 80), flashes=3, speed=0.25):
    """
    Brief bright pulses for visual alerts or reminders.
    Default: three red flashes, 0.25 s each.
    """
    for _ in range(flashes):
        set_color(*color, brightness=1.0)
        time.sleep(speed)
        set_color(0, 0, 0, 0)
        time.sleep(speed)
