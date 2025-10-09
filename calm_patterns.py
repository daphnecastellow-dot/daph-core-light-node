# calm_patterns.py
# Extra breathing and calming light routines
# Author: Daphne Castellow
# License: MIT

import time
from neopixel import NeoPixel
import machine

pin = machine.Pin(4, machine.Pin.OUT)
np = NeoPixel(pin, 1)

def set_color(r, g, b, brightness=0.5):
    np[0] = (int(r*brightness), int(g*brightness), int(b*brightness))
    np.write()

def slow_breath(color=(255, 215, 0), cycles=5, speed=0.1):
    """A slower, softer breathing pattern for relaxation."""
    for _ in range(cycles):
        for i in range(0, 101, 2):
            set_color(*color, i/100)
            time.sleep(speed)
        for i in range(100, -1, -2):
            set_color(*color, i/100)
            time.sleep(speed)

def color_wave(colors, cycles=3, speed=0.08):
    """Gently transition through a list of colors."""
    for _ in range(cycles):
        for c in colors:
            slow_breath(c, cycles=1, speed=speed)
