# morning_mode.py
# Gradual sunrise-style wake-up lighting
# Author: Daphne Castellow
# License: MIT

import time
import machine
from neopixel import NeoPixel

# --- Setup ---
pin = machine.Pin(4, machine.Pin.OUT)
np = NeoPixel(pin, 1)

def set_color(r, g, b, brightness=0.5):
    """Set LED color with brightness control."""
    np[0] = (int(r * brightness), int(g * brightness), int(b * brightness))
    np.write()

# --- Core Sunrise Functions ---

def sunrise_fade(minutes=15):
    """
    Simulate sunrise by brightening from dark red to soft white.
    
    Args:
        minutes: Duration of sunrise in minutes (default: 15)
    
    Color progression: Deep red → Orange → Yellow → Warm white
    Brightness: 10% → 100%
    """
    print(f"[Sunrise] Starting {minutes}-minute sunrise sequence")
    steps = int(minutes * 12)  # 5-second steps
    
    for i in range(steps + 1):
        progress = i / steps
        
        # Color ramp: red → orange → yellow → white
        r = min(255, int(120 + progress * 135))
        g = min(255, int(progress * 180))
        b = int(progress * 120)
        
        # Brightness ramp
        brightness = min(1.0, 0.1 + progress * 0.9)
        
        set_color(r, g, b, brightness)
        time.sleep(5)
    
    print("[Sunrise] Sunrise complete - Good morning!")

def gentle_sunrise(minutes=20):
    """
    Extra gentle sunrise with slower initial phase.
    
    Args:
        minutes: Duration of sunrise in minutes (default: 20)
    
    Uses non-linear brightness curve for more natural awakening.
    """
    print(f"[Gentle Sunrise] Starting {minutes}-minute gentle sunrise")
    steps = int(minutes * 12)
    
    for i in range(steps + 1):
        progress = i / steps
        
        # Non-linear brightness curve (slower start)
        brightness_curve = progress * progress  # Quadratic easing
        brightness = min(1.0, 0.05 + brightness_curve * 0.95)
        
        # Warmer color progression
        r = min(255, int(150 + progress * 105))
        g = min(255, int(progress * 150))
        b = int(progress * 80)
        
        set_color(r, g, b, brightness)
        time.sleep(5)
    
    print("[Gentle Sunrise] Sunrise complete")

def rapid_sunrise(minutes=5):
    """
    Quick sunrise for those who need faster wake-up.
    
    Args:
        minutes: Duration of sunrise in minutes (default: 5)
    
    Faster progression, still gentle on eyes.
    """
    print(f"[Rapid Sunrise] Starting {minutes}-minute rapid sunrise")
    steps = int(minutes * 12)
    
    for i in range(steps + 1):
        progress = i / steps
        
        # Linear brightness
        brightness = 0.2 + progress * 0.8
        
        # Standard sunrise colors
        r = min(255, int(120 + progress * 135))
        g = min(255, int(progress * 180))
        b = int(progress * 120)
        
        set_color(r, g, b, brightness)
        time.sleep(5)
    
    print("[Rapid Sunrise] Sunrise complete")

def arctic_sunrise(minutes=18):
    """
    Cool-toned sunrise inspired by arctic dawn.
    
    Args:
        minutes: Duration of sunrise in minutes (default: 18)
    
    Color progression: Purple → Pink → Cool white
    """
    print(f"[Arctic Sunrise] Starting {minutes}-minute arctic sunrise")
    steps = int(minutes * 12)
    
    for i in range(steps + 1):
        progress = i / steps
        
        # Arctic color progression: purple → pink → cool white
        r = min(255, int(100 + progress * 155))
        g = min(255, int(50 + progress * 205))
        b = min(255, int(150 + progress * 105))
        
        # Gentle brightness curve
        brightness = 0.1 + progress * 0.9
        
        set_color(r, g, b, brightness)
        time.sleep(5)
    
    print("[Arctic Sunrise] Sunrise complete")

def tropical_sunrise(minutes=15):
    """
    Vibrant sunrise inspired by tropical dawn.
    
    Args:
        minutes: Duration of sunrise in minutes (default: 15)
    
    Color progression: Deep red → Bright orange → Golden yellow
    """
    print(f"[Tropical Sunrise] Starting {minutes}-minute tropical sunrise")
    steps = int(minutes * 12)
    
    for i in range(steps + 1):
        progress = i / steps
        
        # Vibrant tropical colors
        r = 255
        g = min(255, int(progress * 200))
        b = max(0, int(100 - progress * 100))
        
        # Dynamic brightness
        brightness = 0.15 + progress * 0.85
        
        set_color(r, g, b, brightness)
        time.sleep(5)
    
    print("[Tropical Sunrise] Sunrise complete")

def dawn_simulator(wake_time_minutes=30, hold_time_minutes=5):
    """
    Complete dawn simulation with pre-wake and post-wake phases.
    
    Args:
        wake_time_minutes: Target wake time (default: 30 min sunrise)
        hold_time_minutes: Time to hold full brightness (default: 5)
    
    Phases:
    1. Deep sleep phase (very dim red)
    2. Sunrise phase (gradual brightening)
    3. Wake phase (full bright warm light)
    """
    print(f"[Dawn Simulator] Starting full dawn cycle")
    
    # Phase 1: Deep sleep (5 minutes, very dim red)
    print("[Dawn] Phase 1: Deep sleep preservation")
    for _ in range(60):  # 5 minutes in 5-second steps
        set_color(80, 0, 0, brightness=0.05)
        time.sleep(5)
    
    # Phase 2: Sunrise
    print(f"[Dawn] Phase 2: Sunrise ({wake_time_minutes} minutes)")
    sunrise_fade(minutes=wake_time_minutes)
    
    # Phase 3: Wake phase (hold bright)
    print(f"[Dawn] Phase 3: Wake phase ({hold_time_minutes} minutes)")
    set_color(255, 220, 180, brightness=1.0)
    time.sleep(hold_time_minutes * 60)
    
    print("[Dawn] Dawn simulation complete - Time to start your day!")

def energy_boost():
    """
    Bright, energizing sequence for already-awake mornings.
    Quick transition to bright cool white.
    """
    print("[Energy Boost] Starting energizing sequence")
    
    # Quick ramp to bright cool white
    for i in range(20):
        progress = i / 20
        brightness = 0.3 + progress * 0.7
        
        # Cool energizing white
        r = int(200 + progress * 55)
        g = int(220 + progress * 35)
        b = int(255)
        
        set_color(r, g, b, brightness)
        time.sleep(1)
    
    print("[Energy Boost] Ready for the day!")
    time.sleep(30)  # Hold for 30 seconds

def progressive_alarm(alarm_minutes=10, pulse_interval_seconds=30):
    """
    Progressive alarm that pulses with increasing intensity.
    
    Args:
        alarm_minutes: Total alarm duration (default: 10)
        pulse_interval_seconds: Time between pulses (default: 30)
    
    Pulses become brighter and more frequent as time progresses.
    """
    print(f"[Progressive Alarm] Starting {alarm_minutes}-minute alarm")
    
    total_seconds = alarm_minutes * 60
    elapsed = 0
    pulse_count = 0
    
    while elapsed < total_seconds:
        pulse_count += 1
        progress = elapsed / total_seconds
        
        # Increasing brightness for each pulse
        max_brightness = 0.3 + progress * 0.7
        
        # Pulse effect
        for i in range(10):
            brightness = (i / 10) * max_brightness
            set_color(255, 100, 0, brightness)
            time.sleep(0.1)
        
        for i in range(10, 0, -1):
            brightness = (i / 10) * max_brightness
            set_color(255, 100, 0, brightness)
            time.sleep(0.1)
        
        # Wait before next pulse (decreasing interval)
        wait_time = max(5, pulse_interval_seconds * (1 - progress))
        time.sleep(wait_time)
        elapsed += 2 + wait_time  # 2 seconds for pulse + wait time
        
        print(f"[Progressive Alarm] Pulse {pulse_count} - {int(progress*100)}% intensity")
    
    # Final state: steady bright
    set_color(255, 200, 150, brightness=1.0)
    print("[Progressive Alarm] Alarm complete - Wake up!")

# --- Preset Morning Modes ---

MORNING_PRESETS = {
    "standard_sunrise": lambda: sunrise_fade(minutes=15),
    "gentle_sunrise": lambda: gentle_sunrise(minutes=20),
    "rapid_sunrise": lambda: rapid_sunrise(minutes=5),
    "arctic_sunrise": lambda: arctic_sunrise(minutes=18),
    "tropical_sunrise": lambda: tropical_sunrise(minutes=15),
    "full_dawn": lambda: dawn_simulator(wake_time_minutes=30, hold_time_minutes=5),
    "energy_boost": lambda: energy_boost(),
    "progressive_alarm": lambda: progressive_alarm(alarm_minutes=10),
}

def start_morning_mode(preset_name):
    """
    Start a preset morning wake-up sequence.
    
    Args:
        preset_name: Name from MORNING_PRESETS
    """
    if preset_name in MORNING_PRESETS:
        print(f"\n{'='*50}")
        print(f"Morning Mode: {preset_name}")
        print(f"{'='*50}\n")
        MORNING_PRESETS[preset_name]()
    else:
        print(f"[Error] Unknown preset: {preset_name}")
        print(f"Available presets: {', '.join(MORNING_PRESETS.keys())}")

# --- Helper Functions ---

def test_sunrise(seconds=30):
    """Quick test of sunrise effect (30 seconds)."""
    print("[Test] Running 30-second sunrise test")
    steps = 30
    
    for i in range(steps + 1):
        progress = i / steps
        r = min(255, int(120 + progress * 135))
        g = min(255, int(progress * 180))
        b = int(progress * 120)
        brightness = 0.1 + progress * 0.9
        
        set_color(r, g, b, brightness)
        time.sleep(1)
    
    print("[Test] Test complete")

def fade_to_off(duration_seconds=10):
    """Gentle fade to off."""
    print("[Fade] Fading to off...")
    steps = duration_seconds
    
    # Get current color (approximation)
    for i in range(steps, -1, -1):
        brightness = i / steps
        set_color(255, 220, 180, brightness)
        time.sleep(1)
    
    set_color(0, 0, 0, 0)
    print("[Fade] Off")

# --- Scheduler Integration ---

def schedule_sunrise(wake_hour, wake_minute, sunrise_minutes=15):
    """
    Schedule sunrise to complete at specified wake time.
    
    Args:
        wake_hour: Hour to wake (24-hour format)
        wake_minute: Minute to wake
        sunrise_minutes: Duration of sunrise (default: 15)
    
    Note: Requires continuous running. Consider using RTC and deep sleep
    for production use.
    """
    import time
    
    while True:
        current_time = time.localtime()
        current_hour = current_time[3]
        current_minute = current_time[4]
        
        # Calculate start time (sunrise_minutes before wake time)
        start_hour = wake_hour
        start_minute = wake_minute - sunrise_minutes
        
        if start_minute < 0:
            start_minute += 60
            start_hour -= 1
        
        if start_hour < 0:
            start_hour += 24
        
        # Check if it's time to start
        if current_hour == start_hour and current_minute == start_minute:
            print(f"[Scheduler] Starting sunrise for {wake_hour:02d}:{wake_minute:02d} wake time")
            sunrise_fade(minutes=sunrise_minutes)
            
            # Sleep until next day to avoid re-triggering
            time.sleep(86400)  # 24 hours
        
        # Check every minute
        time.sleep(60)

# --- Demo Mode ---

def demo_morning_modes():
    """Quick demo of various sunrise modes."""
    print("Morning Mode Demo - Starting...\n")
    
    demos = [
        ("10-second sunrise test", lambda: test_sunrise(seconds=10)),
        ("10-second gentle sunrise", lambda: gentle_sunrise(minutes=0.17)),
        ("Quick energy boost", lambda: energy_boost()),
    ]
    
    for name, func in demos:
        print(f"Demo: {name}")
        func()
        time.sleep(2)
        fade_to_off(duration_seconds=3)
        time.sleep(1)
    
    print("\nMorning Mode Demo - Complete")

# --- Main Execution ---

if __name__ == "__main__":
    print("Morning Mode v1.0 - Wake-Up Light System")
    print("Available presets:", list(MORNING_PRESETS.keys()))
    print()
    
    # Run demo or specific mode
    # demo_morning_modes()
    start_morning_mode("standard_sunrise")
