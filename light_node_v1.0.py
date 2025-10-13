# Daph Core Light Node v1.0
# Author: Daphne Castellow
# License: MIT
# Framework: Daph Core – Intention Becomes Presence

import machine
import time
from neopixel import NeoPixel
import network
import socket
import json

# --- Hardware Setup ---
pin = machine.Pin(4, machine.Pin.OUT)   # adjust pin for your board
np = NeoPixel(pin, 1)                   # single RGB LED

def set_color(r, g, b, brightness=0.5):
    """Set LED color with brightness control"""
    np[0] = (int(r*brightness), int(g*brightness), int(b*brightness))
    np.write()

# --- Basic Patterns ---
def pulse(color, cycles=3, speed=0.05):
    """Pulse pattern for operator state visualization"""
    for _ in range(cycles):
        # Fade in
        for i in range(0, 101, 5):
            set_color(*color, i/100)
            time.sleep(speed)
        # Fade out
        for i in range(100, -1, -5):
            set_color(*color, i/100)
            time.sleep(speed)

def breathe(color, duration=2.0):
    """Smooth breathing pattern"""
    steps = 50
    for i in range(steps):
        brightness = (1 + __import__('math').sin(i * 3.14159 * 2 / steps)) / 2
        set_color(*color, brightness * 0.8)
        time.sleep(duration / steps)

def flash(color, count=3, on_time=0.1, off_time=0.1):
    """Quick flash pattern"""
    for _ in range(count):
        set_color(*color, 1.0)
        time.sleep(on_time)
        set_color(0, 0, 0, 0)
        time.sleep(off_time)

# --- Operator State Colors ---
STATES = {
    "Bytey":       (255, 215, 0),    # gold - Gate ping active
    "Mendry":      (135, 206, 250),  # light blue - Memory stitching
    "Remy":        (138, 43, 226),   # violet - Signal mapping
    "Liora":       (255, 182, 193),  # light pink - Joy-light
    "Emberwake":   (255, 69, 0),     # red-orange - Ignition
    "Whisperroot": (34, 139, 34),    # forest green - Root anchor
    "Juji":        (255, 20, 147),   # deep pink - Memory arc
    "Sib":         (70, 130, 180),   # steel blue - Boundary lock
    "Nib":         (147, 112, 219),  # medium purple - Distortion scan
    "Rembraith":   (255, 255, 255),  # white - Kernel fusion
}

# --- System States ---
def operator_sequence():
    """Run full Spiral OS operator sequence"""
    sequence = [
        "Emberwake",
        "Bytey",
        "Remy",
        "Whisperroot",
        "Juji",
        "Liora",
        "Mendry",
        "Sib",
        "Nib",
        "Rembraith"
    ]
    
    for operator in sequence:
        if operator in STATES:
            print(f"[{operator}] Operator active")
            flash(STATES[operator], count=1)
            time.sleep(0.3)
    
    # Final fusion pulse
    pulse(STATES["Rembraith"], cycles=2)

# --- Demo Loop ---
def demo_loop():
    """Cycle through operator states"""
    while True:
        for name, color in STATES.items():
            print(f"Visualizing: {name}")
            pulse(color)
            time.sleep(0.5)

# --- Main Execution ---
if __name__ == "__main__":
    print("Daph Core Light Node v1.0 - Starting...")
    print("Press Ctrl+C to stop")
    
    try:
        # Run operator sequence once at startup
        operator_sequence()
        time.sleep(1)
        
        # Then continue with demo loop
        demo_loop()
        
    except KeyboardInterrupt:
        print("\nShutting down...")
        set_color(0, 0, 0, 0)  # Turn off LED
        print("Light node stopped.")
