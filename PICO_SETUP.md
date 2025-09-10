# VS Code + Pico 2 W Setup Instructions

## Quick Reference for Students

### First Time Setup
1. **Clone this repo** and open the folder in VS Code
2. **Install MicroPython extension** (official Raspberry Pi Foundation version)
3. **Connect Pico 2 W** (hold BOOTSEL while plugging in USB)
4. **Configure project**: Ctrl+Shift+P → "MicroPython: Configure Project"

### Running Your Code
- **VS Code method**: Open `light_controller.py` → Ctrl+Shift+P → "MicroPython: Run current file on device"
- **Terminal method**: `mpremote run light_controller.py` (after `pip install mpremote`)
- **Interactive**: Ctrl+Shift+P → "MicroPython: Connect to device"
- **Use the ▶ button** that appears in the top-right when viewing .py files

### Terminal Commands
```bash
# Install command-line tools
pip install mpremote
pip install adafruit-ampy

# Run file directly
mpremote run light_controller.py

# Connect interactively
mpremote connect auto

# Alternative with ampy (need to find port first)
ampy --port /dev/ttyACM0 run light_controller.py
```

### File Organization
- ✅ All your code stays in this GitHub repo folder
- ✅ Edit files normally in VS Code
- ✅ Commit and push to GitHub as usual
- ✅ MicroPython extension handles running code on Pico

### Troubleshooting
- **Pico not detected**: Unplug, hold BOOTSEL, plug in again
- **Extension not working**: Make sure it's the official Raspberry Pi Foundation MicroPython extension
- **Connection issues**: Try "MicroPython: Configure Project" again

### Quick Test
Try this in the MicroPython terminal to test connection:
```python
from machine import Pin
led = Pin(25, Pin.OUT)
led.on()  # LED should turn on
led.off() # LED should turn off
```

Your code files never need to leave this folder!
