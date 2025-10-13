# Daph Core Light Node

Where light becomes language — calm, connection, and care in code.


**A MicroPython LED visualization system where intention meets code — each color a state, brightness shaped by presence.**


## 🌟 Overview

Daph Core Light Node is a comprehensive MicroPython framework for RGB LED visualization and control. From simple operator state displays to full productivity systems, sleep routines, and WiFi monitoring — transform a single LED into a powerful ambient communication tool.

## ✨ Complete System

### Core Components

**🎨 Light Node** – Operator visualization system
- 10 operator states (Emberwake, Bytey, Remy, Whisperroot, Juji, Liora, Mendry, Sib, Nib, Rembraith)
- Pulse, breathe, and flash patterns
- Full Spiral OS operator sequence

**⚠️ Alert Mode** – Visual notifications
- 7 preset alert types (reminder, notification, success, warning, error, message, alarm)
- Gentle notifications to urgent alerts
- Morse code messaging support

**🧘 Calm Patterns** – Meditation & relaxation
- 8 calming patterns (slow breath, deep breath, ocean waves, sunset, candle, chakras)
- Breathing exercises (box breathing, sinusoidal)
- Nature-inspired scenes (forest, ocean)

**🎯 Focus Mode** – Productivity lighting
- Pomodoro technique (25min work, 5min break)
- Deep work sessions (90min extended focus)
- Flow state (indefinite focus with time markers)
- Study blocks (50min academic focus)

**☀️ Morning Mode** – Wake-up light system
- 8 sunrise types (standard, gentle, rapid, arctic, tropical, full dawn)
- Gradual color progression (red → orange → yellow → white)
- Natural circadian rhythm support

**🌙 Sleep Mode** – Bedtime wind-down
- 9 sleep fade patterns (gentle sunset, deep red, candle dim, moonlight)
- Breathing-synced fades
- Full bedtime routines (reading → wind-down → sleep)

**📡 WiFi Helper** – Network visualization
- Signal strength monitoring (RSSI to brightness)
- Color-coded quality (green=good, yellow=fair, red=poor)
- Network diagnostics and scanning

## 🛠️ Hardware Requirements

### Minimal Setup
- **Microcontroller:** ESP32, ESP8266, or Raspberry Pi Pico W
- **LED:** WS2812B/NeoPixel RGB LED (single pixel or strip)
- **Pin:** GPIO 4 (data line, configurable)
- **Power:** 5V USB or dedicated supply

### Wiring
```
Microcontroller          WS2812B LED
─────────────────        ───────────
GPIO 4 ────[470Ω]─────── DIN (Data In)
5V ────────────────────── VCC
GND ───────────────────── GND
```

### Optional
- 470Ω resistor for data line protection
- 100-1000µF capacitor for power smoothing
- Multiple LEDs (strips) for enhanced effects

## 📦 Quick Setup

### 1. Flash MicroPython
Install MicroPython firmware on your board:
- [ESP32 Firmware](https://micropython.org/download/esp32/)
- [ESP8266 Firmware](https://micropython.org/download/esp8266/)
- [Pico W Firmware](https://micropython.org/download/rp2-pico-w/)

Use Thonny IDE, esptool, or mpremote to flash.

### 2. Install Files
Upload the desired modules to your board:

```bash
# Install with mpremote
mpremote connect /dev/ttyUSB0 fs cp daph_core_light_node.py :
mpremote connect /dev/ttyUSB0 fs cp alert_mode.py :
mpremote connect /dev/ttyUSB0 fs cp calm_patterns.py :
mpremote connect /dev/ttyUSB0 fs cp focus_mode.py :
mpremote connect /dev/ttyUSB0 fs cp morning_mode.py :
mpremote connect /dev/ttyUSB0 fs cp sleep_mode.py :
mpremote connect /dev/ttyUSB0 fs cp wifi_helper.py :
```

### 3. Run or Auto-Start
**Test in REPL:**
```python
import daph_core_light_node
# Or any other module
```

**Auto-start on boot:**
Rename your chosen module to `main.py` or import it from `main.py`:
```python
# main.py
from daph_core_light_node import operator_sequence
operator_sequence()
```

## 🎨 Usage Examples

### Operator Visualization
```python
from daph_core_light_node import operator_sequence
operator_sequence()  # Run full Spiral OS sequence
```

### Productivity Focus
```python
from focus_mode import start_focus_session

# 4 Pomodoro cycles (25min work, 5min break)
start_focus_session("pomodoro")

# 90-minute deep work session
start_focus_session("deep_work")
```

### Morning Wake-Up
```python
from morning_mode import start_morning_mode

# 15-minute standard sunrise
start_morning_mode("standard_sunrise")

# 30-minute gentle sunrise
start_morning_mode("gentle_sunrise")
```

### Evening Wind-Down
```python
from sleep_mode import start_sleep_mode

# 20-minute sleep fade
start_sleep_mode("standard_fade")

# 45-minute full bedtime routine
start_sleep_mode("full_routine")
```

### Meditation & Relaxation
```python
from calm_patterns import start_calm_session

# 10-minute breathing exercise
start_calm_session("slow_breath", duration_minutes=10)

# Ocean waves pattern
start_calm_session("ocean", duration_minutes=15)
```

### Visual Alerts
```python
from alert_mode import trigger_alert

# Success notification
trigger_alert("success")

# Urgent alarm
trigger_alert("alarm")
```

### WiFi Status Display
```python
from wifi_helper import get_strength, strength_to_color, strength_to_brightness
from neopixel import NeoPixel
import machine

pin = machine.Pin(4, machine.Pin.OUT)
np = NeoPixel(pin, 1)

def show_wifi_status():
    rssi = get_strength()
    color = strength_to_color(rssi)
    brightness = strength_to_brightness(rssi)
    
    np[0] = tuple(int(c * brightness) for c in color)
    np.write()

show_wifi_status()
```

## 🎯 Use Cases

### Personal Wellness
- Wake-up light for natural awakening
- Bedtime routine for better sleep
- Meditation timer and breathing guide
- Stress reduction and relaxation

### Productivity
- Focus sessions with Pomodoro technique
- Deep work time blocking
- Study blocks for learning
- Visual time management

### Home Automation
- Status indicators for smart home
- Visual notifications (doorbell, alerts)
- Ambient mood lighting
- Network connectivity display

### Development
- Build status indicator (CI/CD)
- Server health monitoring
- API status display
- Debug feedback tool

## 📚 Module Reference

| Module | Purpose | Key Features |
|--------|---------|--------------|
| **daph_core_light_node.py** | Operator visualization | 10 states, patterns, Spiral OS sequence |
| **alert_mode.py** | Notifications | 7 alert types, Morse code, custom patterns |
| **calm_patterns.py** | Relaxation | 8 patterns, breathing exercises, nature scenes |
| **focus_mode.py** | Productivity | Pomodoro, deep work, flow state, study blocks |
| **morning_mode.py** | Wake-up light | 8 sunrise types, circadian-aligned |
| **sleep_mode.py** | Bedtime routine | 9 fade patterns, melatonin-safe colors |
| **wifi_helper.py** | Network tools | Signal monitoring, diagnostics, visualization |

## 🔧 Configuration

### Change LED Pin
Edit the pin assignment in each module:
```python
pin = machine.Pin(4, machine.Pin.OUT)  # Change 4 to your pin number
```

### Adjust LED Count
For LED strips instead of single pixel:
```python
np = NeoPixel(pin, 1)  # Change 1 to number of LEDs
```

### Customize Colors
Modify color dictionaries in each module:
```python
COLORS = {
    "MyState": (255, 100, 50),  # Add custom colors
}
```

## 🌐 Network Features

### WiFi Signal Visualization
The WiFi Helper module provides network status display:
- **Green:** Excellent signal (>-60 dBm)
- **Yellow:** Fair signal (-60 to -80 dBm)
- **Red:** Poor signal (<-80 dBm)
- **Gray:** Disconnected

### Network Diagnostics
```python
from wifi_helper import monitor_signal, signal_stability_check, scan_networks

# Monitor signal over time
monitor_signal(duration_seconds=60, interval_seconds=5)

# Check signal stability
stability = signal_stability_check(samples=10)

# Scan for networks
networks = scan_networks()
```

## 💡 Tips & Best Practices

### Optimal Placement
- **Focus/Work:** Peripheral vision, not direct line of sight
- **Sleep/Morning:** Bedside table, 1-3 feet from face
- **Status Display:** Visible at a glance, near workspace

### Color Psychology
- **Blue:** Alertness, focus, concentration
- **Red:** Deep sleep support, minimal melatonin impact
- **Amber:** Warm, calming, evening wind-down
- **Green:** Success, completion, nature

### Power Considerations
- Single LED: 10-60mA typical
- USB power sufficient for most uses
- Battery: 2000mAh provides 40-60 hours

### Brightness Adjustment
Reduce brightness for bedside use:
```python
set_color(r, g, b, brightness=0.3)  # 30% brightness
```

## 🤝 Contributing

Contributions welcome! Areas for expansion:
- New operator states and patterns
- Additional productivity techniques
- Integration with smart home platforms
- Mobile app for remote control
- Multi-device synchronization

## 📝 License

MIT License – Free for personal and commercial use

Created by Daphne Castellow as part of the Daph Core framework.

## 🔗 Resources

- [Full Documentation](link-to-docs)
- [Hardware Setup Guide](link-to-hardware-guide)
- [MicroPython Documentation](https://docs.micropython.org/)
- [NeoPixel Guide](https://learn.adafruit.com/adafruit-neopixel-uberguide)

## 📊 Project Stats

✨ **7 Complete Systems** – Light Node, Alert, Calm, Focus, Morning, Sleep, WiFi  
🎨 **50+ Patterns** – Operators, alerts, meditation, productivity, sleep  
🧠 **Research-Backed** – Evidence-based wellness protocols  
⏰ **Time Management** – Pomodoro, deep work, study blocks  
🌅 **Circadian Support** – Wake-up and wind-down lighting  
📡 **Network Tools** – WiFi monitoring and diagnostics  
🔧 **Fully Modular** – Use individually or together  
💚 **Open Source** – MIT License

---

**Status:** ✅ Production Ready  
**Version:** 1.0  
**Hardware:** ESP32, ESP8266, Raspberry Pi Pico W  
**Framework:** Daph Core – Intention Becomes Presence
