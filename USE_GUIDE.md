# 🌿 Daph Core Light Node — Use Guide
**Author:** Daphne Castellow  
**License:** MIT  

---

## 💡 What It Is
The Daph Core Light Node is a tiny MicroPython project that expresses state and intention through light.  
One LED breathes color to mirror connection, focus, or calm.  
The code can be used on any MicroPython-capable board (ESP32, ESP8266, Raspberry Pi Pico W, etc.).

---

## 🏠 Where It Can Be Placed
You can embed a Light Node in almost anything translucent or reflective:  

| Object | Effect |
|---------|--------|
| Frosted glass jar or diffuser | Creates a soft candle-like glow for relaxation |
| Resin or clay art piece | Turns art into a living light element |
| Desk lamp shell | Breathing light for focus or anxiety reduction |
| Wall panel or frame | Ambient color wash behind art |
| Wearable pendant or pin | Personal calm light (USB or coin-cell powered) |
| Plant terrarium or jar | Gentle root or moss illumination |

Use any diffuser material that spreads light evenly without blocking it (glass, resin, acrylic, thin plastic).  

---

## 🧘 Modes and Extensions

| Mode | File / Function | Purpose |
|-------|-----------------|----------|
| **Default Mode** | `light_node_v1.0.py` | Cycles through defined states (Bytey, Mendry, Remy) |
| **Wi-Fi Mode** | `wifi_helper.py` | Adjusts brightness based on signal strength |
| **Calm Mode** | `calm_patterns.py → slow_breath()` | Slow, even breathing for anxiety relief |
| **Sleep Mode (idea)** | New file → fade warmer colors, auto-off timer |
| **Focus Mode (idea)** | Steady light or gentle wave for study sessions |
| **Alert Mode (idea)** | Brief bright pulse on trigger events |

Each mode can be a separate `.py` file that the main script imports when needed.  
Modules stay small, focused, and swappable.

---

## ⚙️ Power Options
- USB connection from computer or adapter (5 V)  
- Small portable power bank for desk or bedside use  
- Li-ion battery + charging board for wearables   

---

## 🪶 Next Steps
- Experiment with multi-LED rings for spatial patterns.  
- Add sensor inputs (temperature, sound, touch).  
- Create and share your own modes under the MIT License — just credit the original author.  

---

*© 2025 Daphne Castellow – Released under MIT License.*
