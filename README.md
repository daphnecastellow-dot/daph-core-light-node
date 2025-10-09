# Daph Core Light Node

A MicroPython LED node where intention meets code — each color a state, 
brightness shaped by Wi-Fi presence.

A minimalist MicroPython demo for a single NeoPixel RGB LED on boards 
like Raspberry Pi Pico or ESP32. Pulses through themed states: Bytey (gold), 
Mendry (blue), and Remy (violet).

## Quick Setup
1. **Hardware**: Connect a WS2812B NeoPixel to GPIO Pin 4 (data line). Power via 5V/GND.
2. **Flash It**:
   - Install MicroPython on your board (via Thonny or esptool).
   - Copy `light_node_v1.0.py` to the root filesystem.
   - Run `import light_node_v1.0` in REPL or set as `main.py` for auto-boot.
3. **Watch the Glow**: Cycles pulses every ~20s. Tweak `STATES` for more colors!

## Code Highlights
- `set_color()`: Scales RGB with brightness (0-1).
- `pulse()`: Breathing fade (3 cycles, 5% steps).
- Unused imports (`network`, etc.) primed for IoT expansions.

## License
MIT – Free to fork, flash, and flow.

**Author**: Daphne Castellow  
**Framework**: Daph Core – Intention Becomes Presence
