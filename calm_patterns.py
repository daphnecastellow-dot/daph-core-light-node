# calm_patterns.py
# Extra breathing and calming light routines
# Author: Daphne Castellow
# License: MIT

import time
import math
from neopixel import NeoPixel
import machine

pin = machine.Pin(4, machine.Pin.OUT)
np = NeoPixel(pin, 1)

def set_color(r, g, b, brightness=0.5):
    """Set LED color with brightness control."""
    np[0] = (int(r*brightness), int(g*brightness), int(b*brightness))
    np.write()

# --- Core Calming Patterns ---

def slow_breath(color=(255, 215, 0), cycles=5, speed=0.1):
    """
    A slower, softer breathing pattern for relaxation.
    
    Args:
        color: RGB tuple (default: soft gold)
        cycles: Number of breath cycles (default: 5)
        speed: Time between brightness steps (default: 0.1s)
    """
    for _ in range(cycles):
        # Inhale
        for i in range(0, 101, 2):
            set_color(*color, i/100)
            time.sleep(speed)
        # Exhale
        for i in range(100, -1, -2):
            set_color(*color, i/100)
            time.sleep(speed)

def color_wave(colors, cycles=3, speed=0.08):
    """
    Gently transition through a list of colors.
    
    Args:
        colors: List of RGB tuples
        cycles: Number of times to cycle through colors (default: 3)
        speed: Transition speed (default: 0.08s)
    """
    for _ in range(cycles):
        for c in colors:
            slow_breath(c, cycles=1, speed=speed)

def deep_breath(color=(100, 150, 255), hold_time=2.0, speed=0.15):
    """
    Box breathing pattern: inhale (4s), hold (2s), exhale (4s), hold (2s).
    
    Args:
        color: RGB tuple (default: calming blue)
        hold_time: Duration to hold at peak and bottom (default: 2.0s)
        speed: Breathing rate (default: 0.15s per step)
    """
    steps = 30
    
    # Inhale
    for i in range(steps):
        brightness = i / steps
        set_color(*color, brightness=brightness * 0.7)
        time.sleep(speed)
    
    # Hold (full)
    time.sleep(hold_time)
    
    # Exhale
    for i in range(steps, -1, -1):
        brightness = i / steps
        set_color(*color, brightness=brightness * 0.7)
        time.sleep(speed)
    
    # Hold (empty)
    time.sleep(hold_time)

def sinusoidal_breath(color=(255, 200, 150), duration=8.0, cycles=5):
    """
    Ultra-smooth breathing using sine wave for natural rhythm.
    
    Args:
        color: RGB tuple (default: warm amber)
        duration: Duration of one complete breath cycle (default: 8.0s)
        cycles: Number of breath cycles (default: 5)
    """
    steps = 60
    step_time = duration / steps
    
    for _ in range(cycles):
        for step in range(steps):
            # Sine wave from 0 to 1 and back
            brightness = (1 + math.sin((step / steps) * 2 * math.pi - math.pi/2)) / 2
            set_color(*color, brightness=brightness * 0.6)
            time.sleep(step_time)

def gentle_pulse(color=(200, 150, 255), min_brightness=0.1, max_brightness=0.5, speed=0.12):
    """
    Very gentle, continuous pulsing - perfect for ambient meditation.
    
    Args:
        color: RGB tuple (default: soft lavender)
        min_brightness: Minimum brightness level (default: 0.1)
        max_brightness: Maximum brightness level (default: 0.5)
        speed: Pulse rate (default: 0.12s)
    """
    while True:
        # Fade up
        for i in range(20):
            brightness = min_brightness + (max_brightness - min_brightness) * (i / 20)
            set_color(*color, brightness=brightness)
            time.sleep(speed)
        
        # Fade down
        for i in range(20, -1, -1):
            brightness = min_brightness + (max_brightness - min_brightness) * (i / 20)
            set_color(*color, brightness=brightness)
            time.sleep(speed)

def sunset_fade(duration=180.0):
    """
    Gradual warm-to-cool transition over 3 minutes, mimicking sunset.
    
    Args:
        duration: Total duration in seconds (default: 180s = 3 minutes)
    """
    steps = 200
    step_time = duration / steps
    
    for step in range(steps):
        progress = step / steps
        
        # Transition from warm orange to deep blue
        r = int(255 * (1 - progress) + 20 * progress)
        g = int(140 * (1 - progress) + 40 * progress)
        b = int(0 * (1 - progress) + 80 * progress)
        
        brightness = 0.8 * (1 - progress * 0.7)  # Gradually dim
        set_color(r, g, b, brightness=brightness)
        time.sleep(step_time)
    
    # Final state: very dim blue
    set_color(20, 40, 80, brightness=0.2)

def ocean_waves(cycles=10, wave_speed=0.08):
    """
    Alternating teal/blue pattern like gentle ocean waves.
    
    Args:
        cycles: Number of wave cycles (default: 10)
        wave_speed: Speed of wave motion (default: 0.08s)
    """
    colors = [
        (0, 180, 200),    # Teal
        (50, 150, 255),   # Light blue
        (0, 120, 180),    # Deep teal
        (80, 180, 255),   # Sky blue
    ]
    
    for _ in range(cycles):
        for color in colors:
            slow_breath(color, cycles=1, speed=wave_speed)

def forest_ambiance(duration=120.0):
    """
    Slow shifts through greens and earth tones, like a forest at dusk.
    
    Args:
        duration: Total duration in seconds (default: 120s = 2 minutes)
    """
    colors = [
        (50, 120, 40),    # Deep forest green
        (80, 150, 60),    # Moss green
        (100, 180, 80),   # Light green
        (120, 140, 60),   # Yellow-green
        (80, 120, 50),    # Sage
        (60, 100, 45),    # Dark sage
    ]
    
    steps_per_color = 40
    total_steps = len(colors) * steps_per_color
    step_time = duration / total_steps
    
    for color in colors:
        # Fade in to color
        for step in range(steps_per_color):
            brightness = (step / steps_per_color) * 0.5
            set_color(*color, brightness=brightness)
            time.sleep(step_time)

def candle_flicker(color=(255, 147, 41), duration=60.0):
    """
    Subtle random variations like a candle flame - very calming.
    
    Args:
        color: RGB tuple (default: warm candle orange)
        duration: Duration to run in seconds (default: 60s)
    """
    import random
    
    start_time = time.time()
    base_brightness = 0.4
    
    while time.time() - start_time < duration:
        # Random flicker
        variation = random.uniform(-0.15, 0.15)
        brightness = base_brightness + variation
        brightness = max(0.2, min(0.6, brightness))  # Clamp
        
        set_color(*color, brightness=brightness)
        time.sleep(random.uniform(0.05, 0.15))

def chakra_sequence(cycles=2, hold_time=15.0):
    """
    Cycle through the seven chakra colors with pauses.
    
    Args:
        cycles: Number of complete chakra sequences (default: 2)
        hold_time: Time to hold each chakra color (default: 15s)
    """
    chakras = [
        ("Root", (255, 0, 0)),        # Red
        ("Sacral", (255, 127, 0)),    # Orange
        ("Solar Plexus", (255, 255, 0)),  # Yellow
        ("Heart", (0, 255, 0)),       # Green
        ("Throat", (0, 191, 255)),    # Light blue
        ("Third Eye", (75, 0, 130)),  # Indigo
        ("Crown", (148, 0, 211)),     # Violet
    ]
    
    for _ in range(cycles):
        for name, color in chakras:
            print(f"[Chakra] {name}")
            
            # Gentle fade in
            for i in range(30):
                brightness = (i / 30) * 0.6
                set_color(*color, brightness=brightness)
                time.sleep(0.1)
            
            # Hold
            time.sleep(hold_time - 6)  # Account for fade times
            
            # Gentle fade out
            for i in range(30, -1, -1):
                brightness = (i / 30) * 0.6
                set_color(*color, brightness=brightness)
                time.sleep(0.1)
            
            time.sleep(1)  # Brief pause between chakras

# --- Preset Calming Patterns ---

CALM_PRESETS = {
    "slow_breath": lambda: slow_breath((200, 180, 255), cycles=10),
    "deep_breath": lambda: deep_breath((100, 150, 255), hold_time=2.0),
    "ocean": lambda: ocean_waves(cycles=15),
    "forest": lambda: forest_ambiance(duration=120),
    "sunset": lambda: sunset_fade(duration=180),
    "candle": lambda: candle_flicker(duration=60),
    "chakras": lambda: chakra_sequence(cycles=1, hold_time=15),
    "sine_breath": lambda: sinusoidal_breath((255, 200, 150), duration=8, cycles=10),
}

def start_calm_session(pattern_name, duration_minutes=5):
    """
    Start a timed calming session.
    
    Args:
        pattern_name: Name from CALM_PRESETS
        duration_minutes: How long to run (default: 5 minutes)
    """
    print(f"[Calm Session] Starting: {pattern_name} for {duration_minutes} min")
    
    if pattern_name == "gentle_pulse":
        # Special case: runs indefinitely, needs timer
        start_time = time.time()
        duration_seconds = duration_minutes * 60
        
        while time.time() - start_time < duration_seconds:
            gentle_pulse((200, 150, 255), speed=0.12)
    
    elif pattern_name in CALM_PRESETS:
        CALM_PRESETS[pattern_name]()
    
    else:
        print(f"[Error] Unknown pattern: {pattern_name}")
        return
    
    # Gentle fade to off
    print("[Calm Session] Complete - fading out...")
    for i in range(30, -1, -1):
        set_color(100, 100, 150, brightness=(i/30) * 0.3)
        time.sleep(0.1)
    
    set_color(0, 0, 0, 0)
    print("[Calm Session] Ended")

# --- Demo Mode ---

def demo_calm_patterns():
    """Demo all calm patterns briefly."""
    print("Calm Patterns Demo - Starting...\n")
    
    demos = [
        ("Slow Breath", lambda: slow_breath((255, 200, 150), cycles=3)),
        ("Deep Breath", lambda: deep_breath((100, 150, 255), hold_time=1.0)),
        ("Ocean Waves", lambda: ocean_waves(cycles=3)),
        ("Candle Flicker", lambda: candle_flicker(duration=10)),
        ("Sine Breath", lambda: sinusoidal_breath((200, 180, 255), duration=6, cycles=2)),
    ]
    
    for name, func in demos:
        print(f"Demo: {name}")
        func()
        time.sleep(1)
    
    print("\nCalm Patterns Demo - Complete")

# --- Main Execution ---

if __name__ == "__main__":
    print("Calm Patterns v1.0 - Ready for relaxation")
    print("Available patterns:", list(CALM_PRESETS.keys()))
    
    # Run demo
    demo_calm_patterns()
