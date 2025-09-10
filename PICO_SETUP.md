# VS Code + Pico 2 W Setup Instructions

## Quick Reference for Students

### First Time Setup
1. **Clone this repo** and open the folder in VS Code
2. **Install MicroPico extension** (`paulober.pico-w-go`)
3. **Connect Pico 2 W** (hold BOOTSEL while plugging in USB)
4. **Configure project**: Ctrl+Shift+P → "MicroPico: Configure Project"

### Running Your Code
- **VS Code method**: Open `light_controller.py` → Ctrl+Shift+P → "MicroPico: Run current file"
- **Alternative**: Click the ▶ button that appears in the top-right when viewing .py files
- **Terminal method**: `mpremote run light_controller.py` (after `pip install mpremote`)
- **Interactive**: Ctrl+Shift+P → "MicroPico: Connect"

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
- ✅ MicroPico extension handles running code on Pico

### Troubleshooting
- **Pico not detected**: Unplug, hold BOOTSEL, plug in again
- **Extension not working**: Make sure it's **MicroPico by paulober** (not other MicroPython extensions)
- **Connection issues**: Try "MicroPico: Configure Project" again

### Quick Test
Try this in the MicroPython terminal to test connection:
```python
from machine import Pin
led = Pin(25, Pin.OUT)
led.on()  # LED should turn on
led.off() # LED should turn off
```

Your code files never need to leave this folder!
