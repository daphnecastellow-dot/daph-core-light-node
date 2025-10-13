# sleep_mode.py
# Gentle warm fade for bedtime
# Author: Daphne Castellow
# License: MIT

import time
import machine
from neopixel import NeoPixel

# --- Setup ---
pin = machine.Pin(4, machine.Pin.OUT)
np = NeoPixel(pin, 1)

def set_color(r, g, b, brightness=0.3):
    """Set NeoPixel color with adjustable brightness."""
    np[0] = (int(r * brightness), int(g * brightness), int(b * brightness))
    np.write()

# --- Core Sleep Functions ---

def sleep_fade(color=(255, 160, 80), minutes=20):
    """
    Warm amber light that fades slowly to darkness.
    
    Args:
        color: RGB tuple (default: warm amber)
        minutes: Duration in minutes (default: 20)
    
    Each step dims every 5 seconds, mimicking natural sunset.
    """
    print(f"[Sleep Mode] Starting {minutes}-minute fade to sleep")
    steps = int(minutes * 12)  # 12 steps per minute
    
    for i in range(steps, -1, -1):
        level = i / steps
        set_color(*color, brightness=0.3 * level)
        time.sleep(5)
    
    # Turn off completely
    set_color(0, 0, 0, 0)
    print("[Sleep Mode] Lights out - Goodnight")

def gentle_sunset(minutes=30):
    """
    Extended sunset with color progression from warm orange to deep red.
    
    Args:
        minutes: Duration in minutes (default: 30)
    
    Color shifts: Orange → Amber → Deep red → Off
    Mimics natural sunset color temperature changes.
    """
    print(f"[Gentle Sunset] Starting {minutes}-minute sunset sequence")
    steps = int(minutes * 12)
    
    for i in range(steps, -1, -1):
        progress = i / steps
        
        # Color progression: orange → amber → deep red
        r = int(255 * progress)
        g = int(160 * progress * progress)  # Faster fade for green
        b = int(30 * progress)
        
        brightness = 0.4 * progress
        set_color(r, g, b, brightness)
        time.sleep(5)
    
    set_color(0, 0, 0, 0)
    print("[Gentle Sunset] Sunset complete")

def quick_sleep(minutes=10):
    """
    Faster fade for when you're already sleepy.
    
    Args:
        minutes: Duration in minutes (default: 10)
    
    Rapid but still gentle transition to darkness.
    """
    print(f"[Quick Sleep] Starting {minutes}-minute quick fade")
    steps = int(minutes * 12)
    
    for i in range(steps, -1, -1):
        level = i / steps
        # Warm red-orange
        set_color(255, 100, 30, brightness=0.3 * level)
        time.sleep(5)
    
    set_color(0, 0, 0, 0)
    print("[Quick Sleep] Lights out")

def moonlight_glow(minutes=60, final_brightness=0.05):
    """
    Very dim blue-white glow that stays on as nightlight.
    
    Args:
        minutes: Duration to fade to nightlight level (default: 60)
        final_brightness: Nightlight brightness 0.0-1.0 (default: 0.05)
    
    Fades from warm amber to cool dim glow, then maintains nightlight.
    """
    print(f"[Moonlight] Starting {minutes}-minute fade to nightlight")
    steps = int(minutes * 12)
    
    # Fade from warm to cool
    for i in range(steps, -1, -1):
        progress = i / steps
        
        # Transition from warm amber to cool blue-white
        r = int(255 * progress + 150 * (1 - progress))
        g = int(160 * progress + 180 * (1 - progress))
        b = int(80 * progress + 220 * (1 - progress))
        
        brightness = 0.3 * progress + final_brightness * (1 - progress)
        set_color(r, g, b, brightness)
        time.sleep(5)
    
    # Hold nightlight indefinitely
    print(f"[Moonlight] Nightlight active at {final_brightness*100:.1f}% brightness")
    set_color(150, 180, 220, brightness=final_brightness)

def reading_light_fade(reading_minutes=30, fade_minutes=15):
    """
    Hold comfortable reading light, then fade to sleep.
    
    Args:
        reading_minutes: Time to hold reading light (default: 30)
        fade_minutes: Fade duration after reading (default: 15)
    
    Perfect for bedtime reading routine.
    """
    print(f"[Reading Light] {reading_minutes} min reading, then {fade_minutes} min fade")
    
    # Phase 1: Reading light (warm white)
    print("[Reading Light] Reading phase")
    set_color(255, 220, 180, brightness=0.6)
    time.sleep(reading_minutes * 60)
    
    # Phase 2: Fade to sleep
    print("[Reading Light] Fading to sleep...")
    sleep_fade(color=(255, 160, 80), minutes=fade_minutes)

def campfire_flicker_fade(minutes=25):
    """
    Gentle flickering amber light that slowly fades, like dying campfire.
    
    Args:
        minutes: Total duration in minutes (default: 25)
    
    Combines subtle random variations with gradual fade.
    """
    import random
    
    print(f"[Campfire] Starting {minutes}-minute campfire fade")
    total_steps = int(minutes * 12)
    
    for step in range(total_steps, -1, -1):
        base_level = step / total_steps
        
        # Random flicker variation
        flicker = random.uniform(0.85, 1.0)
        brightness = 0.35 * base_level * flicker
        
        # Warm campfire colors
        r = 255
        g = int(100 + 60 * base_level)
        b = int(20 * base_level)
        
        set_color(r, g, b, brightness)
        time.sleep(random.uniform(4.5, 5.5))  # Slight timing variation
    
    set_color(0, 0, 0, 0)
    print("[Campfire] Fire extinguished")

def progressive_sleep(alert_minutes=10, wind_down_minutes=15, sleep_minutes=20):
    """
    Three-phase sleep preparation: Alert → Wind down → Sleep.
    
    Args:
        alert_minutes: Initial moderate light phase (default: 10)
        wind_down_minutes: Dimming warm light (default: 15)
        sleep_minutes: Final fade to darkness (default: 20)
    
    Total: 45 minutes of structured bedtime routine.
    """
    print(f"[Progressive Sleep] Starting 3-phase routine")
    print(f"Phase 1: {alert_minutes} min, Phase 2: {wind_down_minutes} min, Phase 3: {sleep_minutes} min")
    
    # Phase 1: Alert phase (moderate warm white)
    print("[Progressive] Phase 1: Evening activities")
    set_color(255, 200, 150, brightness=0.5)
    time.sleep(alert_minutes * 60)
    
    # Phase 2: Wind down (dimmer amber)
    print("[Progressive] Phase 2: Wind down")
    steps = int(wind_down_minutes * 12)
    for i in range(steps):
        progress = i / steps
        brightness = 0.5 - (0.2 * progress)  # 0.5 → 0.3
        set_color(255, 180, 100, brightness=brightness)
        time.sleep(5)
    
    # Phase 3: Sleep fade (deep amber to off)
    print("[Progressive] Phase 3: Sleep fade")
    sleep_fade(color=(255, 120, 50), minutes=sleep_minutes)

def breathe_to_sleep(cycles=30, cycle_duration=8):
    """
    Breathing pattern that slows to help regulate breathing and sleep.
    
    Args:
        cycles: Number of breathing cycles (default: 30 = ~4 minutes)
        cycle_duration: Seconds per breath cycle (default: 8)
    
    Visual breathing guide that gradually dims and slows.
    """
    print(f"[Breathe to Sleep] {cycles} breathing cycles")
    
    for cycle in range(cycles, 0, -1):
        progress = cycle / cycles
        
        # Gradual slowing of breath
        current_duration = cycle_duration + (12 - cycle_duration) * (1 - progress)
        
        # Inhale
        for i in range(20):
            brightness = 0.1 + (0.3 * progress * (i / 20))
            set_color(255, 150, 80, brightness=brightness)
            time.sleep(current_duration / 40)
        
        # Exhale
        for i in range(20, 0, -1):
            brightness = 0.1 + (0.3 * progress * (i / 20))
            set_color(255, 150, 80, brightness=brightness)
            time.sleep(current_duration / 40)
    
    # Final fade out
    for i in range(20, -1, -1):
        set_color(255, 150, 80, brightness=0.1 * (i/20))
        time.sleep(0.2)
    
    set_color(0, 0, 0, 0)
    print("[Breathe to Sleep] Breathing complete - Sleep well")

# --- Preset Sleep Modes ---

SLEEP_PRESETS = {
    "standard_sleep": lambda: sleep_fade(minutes=20),
    "gentle_sunset": lambda: gentle_sunset(minutes=30),
    "quick_sleep": lambda: quick_sleep(minutes=10),
    "moonlight": lambda: moonlight_glow(minutes=60, final_brightness=0.05),
    "reading_fade": lambda: reading_light_fade(reading_minutes=30, fade_minutes=15),
    "campfire": lambda: campfire_flicker_fade(minutes=25),
    "progressive": lambda: progressive_sleep(alert_minutes=10, wind_down_minutes=15, sleep_minutes=20),
    "breathe": lambda: breathe_to_sleep(cycles=30, cycle_duration=8),
}

def start_sleep_mode(preset_name):
    """
    Start a preset sleep/bedtime sequence.
    
    Args:
        preset_name: Name from SLEEP_PRESETS
    """
    if preset_name in SLEEP_PRESETS:
        print(f"\n{'='*50}")
        print(f"Sleep Mode: {preset_name}")
        print(f"{'='*50}\n")
        SLEEP_PRESETS[preset_name]()
    else:
        print(f"[Error] Unknown preset: {preset_name}")
        print(f"Available presets: {', '.join(SLEEP_PRESETS.keys())}")

# --- Helper Functions ---

def night_light(brightness=0.05, color=(150, 180, 220)):
    """
    Static nightlight mode - stays on indefinitely.
    
    Args:
        brightness: Light intensity 0.0-1.0 (default: 0.05)
        color: RGB tuple (default: cool blue-white)
    """
    print(f"[Night Light] Active at {brightness*100:.1f}% brightness")
    print("[Night Light] Press Ctrl+C to turn off")
    
    set_color(*color, brightness=brightness)
    
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        print("\n[Night Light] Turning off...")
        set_color(0, 0, 0, 0)

def emergency_off():
    """Immediate lights off."""
    print("[Emergency] Lights off immediately")
    set_color(0, 0, 0, 0)

# --- Scheduler Integration ---

def schedule_bedtime(bedtime_hour, bedtime_minute, fade_minutes=20):
    """
    Schedule sleep fade to complete at specified bedtime.
    
    Args:
        bedtime_hour: Hour for lights out (24-hour format)
        bedtime_minute: Minute for lights out
        fade_minutes: Duration of fade (default: 20)
    """
    import time
    
    print(f"[Scheduler] Bedtime set for {bedtime_hour:02d}:{bedtime_minute:02d}")
    
    while True:
        current_time = time.localtime()
        current_hour = current_time[3]
        current_minute = current_time[4]
        
        # Calculate start time
        start_hour = bedtime_hour
        start_minute = bedtime_minute - fade_minutes
        
        if start_minute < 0:
            start_minute += 60
            start_hour -= 1
        
        if start_hour < 0:
            start_hour += 24
        
        # Check if it's time to start
        if current_hour == start_hour and current_minute == start_minute:
            print(f"[Scheduler] Starting sleep fade for {bedtime_hour:02d}:{bedtime_minute:02d} bedtime")
            sleep_fade(minutes=fade_minutes)
            
            # Sleep until next day
            time.sleep(86400)  # 24 hours
        
        # Check every minute
        time.sleep(60)

# --- Demo Mode ---

def demo_sleep_modes():
    """Quick demo of sleep modes."""
    print("Sleep Mode Demo - Starting...\n")
    
    demos = [
        ("10-second sleep fade", lambda: sleep_fade(minutes=0.17)),
        ("10-second campfire", lambda: campfire_flicker_fade(minutes=0.17)),
        ("6 breathing cycles", lambda: breathe_to_sleep(cycles=6, cycle_duration=4)),
    ]
    
    for name, func in demos:
        print(f"Demo: {name}")
        func()
        time.sleep(2)
    
    print("\nSleep Mode Demo - Complete")

# --- Main Execution ---

if __name__ == "__main__":
    print("Sleep Mode v1.0 - Bedtime Light System")
    print("Available presets:", list(SLEEP_PRESETS.keys()))
    print()
    
    # Run demo or specific mode
    # demo_sleep_modes()
    start_sleep_mode("standard_sleep")
