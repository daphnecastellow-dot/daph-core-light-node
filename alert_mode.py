# alert_mode.py
# Short bright pulses for gentle notifications or reminders
# Author: Daphne Castellow
# License: MIT

import time
import machine
from neopixel import NeoPixel

# --- Setup ---
pin = machine.Pin(4, machine.Pin.OUT)
np = NeoPixel(pin, 1)

def set_color(r, g, b, brightness=1.0):
    """Set NeoPixel color at specified brightness."""
    np[0] = (int(r * brightness), int(g * brightness), int(b * brightness))
    np.write()

# --- Core Alert Functions ---

def pulse_alert(color=(255, 80, 80), flashes=3, speed=0.25):
    """
    Brief bright pulses for visual alerts or reminders.
    
    Args:
        color: RGB tuple (default: soft red)
        flashes: Number of pulses (default: 3)
        speed: Duration of each on/off cycle in seconds (default: 0.25)
    """
    for _ in range(flashes):
        set_color(*color, brightness=1.0)
        time.sleep(speed)
        set_color(0, 0, 0, 0)
        time.sleep(speed)

def double_tap(color=(100, 200, 255), pause=0.15):
    """
    Two quick flashes - gentle 'acknowledgment' pattern.
    
    Args:
        color: RGB tuple (default: light blue)
        pause: Time between taps in seconds (default: 0.15)
    """
    for _ in range(2):
        set_color(*color, brightness=1.0)
        time.sleep(0.1)
        set_color(0, 0, 0, 0)
        time.sleep(pause)

def urgent_flash(color=(255, 0, 0), count=5, speed=0.1):
    """
    Rapid flashing for urgent notifications.
    
    Args:
        color: RGB tuple (default: bright red)
        count: Number of flashes (default: 5)
        speed: Duration of each flash in seconds (default: 0.1)
    """
    for _ in range(count):
        set_color(*color, brightness=1.0)
        time.sleep(speed)
        set_color(0, 0, 0, 0)
        time.sleep(speed)

def success_pulse(color=(0, 255, 100), duration=1.5):
    """
    Smooth fade-in then fade-out - 'success' or 'complete' indicator.
    
    Args:
        color: RGB tuple (default: bright green)
        duration: Total duration in seconds (default: 1.5)
    """
    steps = 30
    step_time = duration / (steps * 2)
    
    # Fade in
    for i in range(steps):
        brightness = i / steps
        set_color(*color, brightness=brightness)
        time.sleep(step_time)
    
    # Fade out
    for i in range(steps, -1, -1):
        brightness = i / steps
        set_color(*color, brightness=brightness)
        time.sleep(step_time)
    
    set_color(0, 0, 0, 0)

def warning_pulse(color=(255, 165, 0), cycles=2):
    """
    Medium-pace pulsing - 'warning' or 'attention needed' pattern.
    
    Args:
        color: RGB tuple (default: orange)
        cycles: Number of complete pulse cycles (default: 2)
    """
    for _ in range(cycles):
        # Fade in
        for brightness in range(0, 101, 10):
            set_color(*color, brightness=brightness/100)
            time.sleep(0.05)
        
        # Hold
        time.sleep(0.2)
        
        # Fade out
        for brightness in range(100, -1, -10):
            set_color(*color, brightness=brightness/100)
            time.sleep(0.05)
        
        time.sleep(0.2)

def heartbeat(color=(255, 50, 100), beats=3):
    """
    Double-pulse pattern resembling a heartbeat.
    
    Args:
        color: RGB tuple (default: pink-red)
        beats: Number of heartbeat cycles (default: 3)
    """
    for _ in range(beats):
        # First beat
        set_color(*color, brightness=1.0)
        time.sleep(0.1)
        set_color(*color, brightness=0.3)
        time.sleep(0.1)
        
        # Second beat
        set_color(*color, brightness=1.0)
        time.sleep(0.1)
        set_color(0, 0, 0, 0)
        time.sleep(0.5)

def morse_pattern(color=(255, 255, 255), pattern="SOS"):
    """
    Flash in Morse code pattern.
    
    Args:
        color: RGB tuple (default: white)
        pattern: String to encode - supports A-Z, 0-9, SOS
    
    Morse timing:
        dot = 0.1s, dash = 0.3s, space between = 0.1s, letter gap = 0.3s
    """
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.'
    }
    
    for char in pattern.upper():
        if char == ' ':
            time.sleep(0.7)  # Word gap
            continue
        
        if char in morse_dict:
            for symbol in morse_dict[char]:
                set_color(*color, brightness=1.0)
                if symbol == '.':
                    time.sleep(0.1)  # Dot
                else:
                    time.sleep(0.3)  # Dash
                set_color(0, 0, 0, 0)
                time.sleep(0.1)  # Symbol gap
            
            time.sleep(0.3)  # Letter gap

# --- Preset Alert Types ---

ALERT_PRESETS = {
    "reminder": lambda: pulse_alert((255, 200, 100), flashes=2, speed=0.3),
    "notification": lambda: double_tap((100, 200, 255)),
    "success": lambda: success_pulse((0, 255, 100)),
    "warning": lambda: warning_pulse((255, 165, 0)),
    "error": lambda: urgent_flash((255, 0, 0), count=4),
    "message": lambda: heartbeat((150, 100, 255), beats=2),
    "alarm": lambda: urgent_flash((255, 0, 0), count=10, speed=0.08),
}

def trigger_alert(alert_type):
    """
    Trigger a preset alert pattern by name.
    
    Args:
        alert_type: String key from ALERT_PRESETS
    """
    if alert_type in ALERT_PRESETS:
        print(f"[Alert] Triggering: {alert_type}")
        ALERT_PRESETS[alert_type]()
    else:
        print(f"[Alert] Unknown type: {alert_type}")
        pulse_alert()  # Default fallback

# --- Demo Mode ---

def demo_all_alerts():
    """Cycle through all alert types for demonstration."""
    print("Alert Mode Demo - Starting...")
    
    for name in ALERT_PRESETS.keys():
        print(f"\nDemo: {name}")
        trigger_alert(name)
        time.sleep(1)
    
    print("\nAlert Mode Demo - Complete")

# --- Main Execution ---

if __name__ == "__main__":
    print("Alert Mode v1.0 - Ready")
    print("Available alerts:", list(ALERT_PRESETS.keys()))
    
    # Run demo
    demo_all_alerts()
