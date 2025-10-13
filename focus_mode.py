# focus_mode.py
# Steady cool-blue light for concentration
# Author: Daphne Castellow
# License: MIT

import time
import machine
from neopixel import NeoPixel

# --- Setup ---
pin = machine.Pin(4, machine.Pin.OUT)
np = NeoPixel(pin, 1)

def set_color(r, g, b, brightness=0.6):
    """Set NeoPixel color with adjustable brightness."""
    np[0] = (int(r * brightness), int(g * brightness), int(b * brightness))
    np.write()

# --- Core Focus Functions ---

def focus_light(color=(135, 206, 250), duration_minutes=None, brightness=0.6):
    """
    Hold a steady cool-blue light to support concentration or study.
    
    Args:
        color: RGB tuple (default: light blue)
        duration_minutes: Session length in minutes (None = indefinite)
        brightness: Light intensity 0.0-1.0 (default: 0.6)
    """
    set_color(*color, brightness=brightness)
    
    if duration_minutes is None:
        # Indefinite focus mode
        print("[Focus Mode] Active indefinitely - Press Ctrl+C to stop")
        try:
            while True:
                time.sleep(60)
        except KeyboardInterrupt:
            print("\n[Focus Mode] Interrupted - Fading out...")
            fade_out(color, brightness)
    else:
        # Timed session with gentle fade-out at the end
        total_seconds = int(duration_minutes * 60)
        print(f"[Focus Mode] Active for {duration_minutes} minutes")
        time.sleep(total_seconds)
        
        print("[Focus Mode] Session complete - Fading out...")
        fade_out(color, brightness)

def pomodoro_session(work_minutes=25, break_minutes=5, cycles=4):
    """
    Pomodoro technique with visual indicators.
    
    Args:
        work_minutes: Work session length (default: 25)
        break_minutes: Break length (default: 5)
        cycles: Number of pomodoro cycles (default: 4)
    """
    print(f"[Pomodoro] Starting {cycles} cycles")
    
    for cycle in range(1, cycles + 1):
        # Work session - steady blue
        print(f"\n[Pomodoro] Cycle {cycle}/{cycles} - WORK TIME ({work_minutes} min)")
        set_color(100, 150, 255, brightness=0.6)  # Cool blue
        time.sleep(work_minutes * 60)
        
        # Work complete - brief green flash
        print(f"[Pomodoro] Work session complete!")
        flash_complete(color=(0, 255, 100))
        
        # Determine break type
        if cycle == cycles:
            # Long break after last cycle
            break_time = break_minutes * 2
            print(f"[Pomodoro] LONG BREAK ({break_time} min)")
        else:
            break_time = break_minutes
            print(f"[Pomodoro] Short break ({break_time} min)")
        
        # Break - warm amber
        set_color(255, 180, 100, brightness=0.4)
        time.sleep(break_time * 60)
        
        # Break complete - brief blue pulse
        if cycle < cycles:
            print(f"[Pomodoro] Break over - Back to work!")
            flash_complete(color=(100, 150, 255))
    
    print("\n[Pomodoro] All cycles complete - Well done!")
    celebration_sequence()
    set_color(0, 0, 0, 0)

def deep_work_session(duration_minutes=90, warmup_minutes=5):
    """
    Extended deep work session with gradual brightness ramp-up.
    
    Args:
        duration_minutes: Total session length (default: 90)
        warmup_minutes: Gradual brightness increase period (default: 5)
    """
    print(f"[Deep Work] Starting {duration_minutes}-minute session")
    
    # Warm-up phase: gradual brightness increase
    print(f"[Deep Work] Warm-up phase ({warmup_minutes} min)")
    warmup_steps = warmup_minutes * 60
    for step in range(warmup_steps):
        brightness = 0.2 + (0.5 * (step / warmup_steps))  # 0.2 to 0.7
        set_color(120, 160, 255, brightness=brightness)
        time.sleep(1)
    
    # Main work session
    work_time = (duration_minutes - warmup_minutes) * 60
    print(f"[Deep Work] Main session in progress...")
    set_color(120, 160, 255, brightness=0.7)
    time.sleep(work_time)
    
    # Session complete
    print("[Deep Work] Session complete - Great work!")
    flash_complete(color=(0, 255, 100), flashes=3)
    fade_out((120, 160, 255), 0.7)

def flow_state(color=(100, 180, 255), check_interval_minutes=30):
    """
    Indefinite focus mode with periodic subtle pulses as time markers.
    
    Args:
        color: RGB tuple (default: medium blue)
        check_interval_minutes: Minutes between pulses (default: 30)
    """
    print("[Flow State] Entering flow state - Ctrl+C to exit")
    interval_seconds = check_interval_minutes * 60
    
    try:
        cycle = 0
        while True:
            cycle += 1
            print(f"[Flow State] Interval {cycle} ({check_interval_minutes} min)")
            
            # Steady light
            set_color(*color, brightness=0.6)
            time.sleep(interval_seconds - 3)  # Account for pulse time
            
            # Subtle pulse marker
            gentle_pulse(color, cycles=1)
    
    except KeyboardInterrupt:
        print(f"\n[Flow State] Exited after {cycle} intervals ({cycle * check_interval_minutes} minutes)")
        fade_out(color, 0.6)

def study_blocks(block_minutes=50, break_minutes=10, blocks=3):
    """
    Study block method (longer than Pomodoro, fewer breaks).
    
    Args:
        block_minutes: Study block length (default: 50)
        break_minutes: Break length (default: 10)
        blocks: Number of study blocks (default: 3)
    """
    print(f"[Study Blocks] {blocks} blocks of {block_minutes} minutes")
    
    for block in range(1, blocks + 1):
        # Study block - cool white
        print(f"\n[Study] Block {block}/{blocks} - STUDY TIME ({block_minutes} min)")
        set_color(200, 210, 255, brightness=0.65)
        time.sleep(block_minutes * 60)
        
        # Block complete
        print(f"[Study] Block {block} complete!")
        flash_complete(color=(100, 255, 150))
        
        if block < blocks:
            # Break time - warm yellow
            print(f"[Study] Break time ({break_minutes} min)")
            set_color(255, 220, 150, brightness=0.4)
            time.sleep(break_minutes * 60)
            print(f"[Study] Break over - Next block starting!")
    
    print("\n[Study] All blocks complete - Excellent work!")
    celebration_sequence()
    set_color(0, 0, 0, 0)

# --- Helper Functions ---

def fade_out(color, initial_brightness):
    """Smooth fade-out sequence."""
    for i in range(100, -1, -5):
        set_color(*color, brightness=initial_brightness * i/100)
        time.sleep(0.1)
    set_color(0, 0, 0, 0)

def flash_complete(color=(0, 255, 100), flashes=2):
    """Brief flash to indicate completion."""
    for _ in range(flashes):
        set_color(*color, brightness=0.8)
        time.sleep(0.15)
        set_color(0, 0, 0, 0)
        time.sleep(0.15)

def gentle_pulse(color, cycles=1):
    """Subtle pulse without disrupting focus."""
    for _ in range(cycles):
        for i in range(60, 80, 2):
            set_color(*color, brightness=i/100)
            time.sleep(0.05)
        for i in range(80, 60, -2):
            set_color(*color, brightness=i/100)
            time.sleep(0.05)

def celebration_sequence():
    """Brief celebration for completing all sessions."""
    colors = [
        (0, 255, 100),   # Green
        (100, 200, 255), # Blue
        (255, 200, 100), # Amber
    ]
    for color in colors:
        set_color(*color, brightness=0.7)
        time.sleep(0.2)
    set_color(0, 0, 0, 0)

# --- Preset Focus Sessions ---

FOCUS_PRESETS = {
    "quick_focus": lambda: focus_light(duration_minutes=15, brightness=0.5),
    "standard_focus": lambda: focus_light(duration_minutes=25, brightness=0.6),
    "deep_work": lambda: deep_work_session(duration_minutes=90),
    "pomodoro": lambda: pomodoro_session(work_minutes=25, break_minutes=5, cycles=4),
    "study_session": lambda: study_blocks(block_minutes=50, break_minutes=10, blocks=3),
    "flow_state": lambda: flow_state(check_interval_minutes=30),
}

def start_focus_session(preset_name):
    """
    Start a preset focus session.
    
    Args:
        preset_name: Name from FOCUS_PRESETS
    """
    if preset_name in FOCUS_PRESETS:
        print(f"\n{'='*50}")
        print(f"Starting: {preset_name}")
        print(f"{'='*50}\n")
        FOCUS_PRESETS[preset_name]()
    else:
        print(f"[Error] Unknown preset: {preset_name}")
        print(f"Available presets: {', '.join(FOCUS_PRESETS.keys())}")

# --- Demo Mode ---

def demo_focus_modes():
    """Brief demo of focus modes."""
    print("Focus Mode Demo - Starting...\n")
    
    demos = [
        ("15-second focus", lambda: focus_light(duration_minutes=0.25, brightness=0.6)),
        ("Quick work/break", lambda: pomodoro_session(work_minutes=0.25, break_minutes=0.15, cycles=1)),
        ("Focus pulse", lambda: gentle_pulse((100, 180, 255), cycles=3)),
    ]
    
    for name, func in demos:
        print(f"Demo: {name}")
        func()
        time.sleep(1)
    
    print("\nFocus Mode Demo - Complete")

# --- Main Execution ---

if __name__ == "__main__":
    print("Focus Mode v1.0 - Productivity Light System")
    print("Available presets:", list(FOCUS_PRESETS.keys()))
    print()
    
    # Run demo or specific session
    # demo_focus_modes()
    start_focus_session("pomodoro")
