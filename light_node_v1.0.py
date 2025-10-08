


# Daph Core Light Node v1.0
# Author: Daphne Castellow
# License: MIT
# Framework: Daph Core – Intention Becomes Presence

import machine, time
from neopixel import NeoPixel
import network, socket, json

# --- Setup ---
pin = machine.Pin(4, machine.Pin.OUT)   # adjust pin for your board
np = NeoPixel(pin, 1)                   # single RGB LED

def set_color(r, g, b, brightness=0.5):
    np[0] = (int(r*brightness), int(g*brightness), int(b*brightness))
    np.write()

# --- Basic patterns ---
def pulse(color, cycles=3, speed=0.05):
    for _ in range(cycles):
        for i in range(0, 101, 5):
            set_color(*color, i/100)
            time.sleep(speed)
        for i in range(100, -1, -5):
            set_color(*color, i/100)
            time.sleep(speed)

# --- Example states ---
STATES = {
    "Bytey":  (255, 215, 0),    # gold
    "Mendry": (135, 206, 250),  # light blue
    "Remy":   (138, 43, 226)    # violet
}

# --- Demo loop ---
while True:
    for name, color in STATES.items():
        pulse(color)
        time.sleep(0.5)
