# Raspberry Pi Pico 2W Setup for CS100

This setup guide has **2 main parts**:
1. **Installing MicroPython firmware** on your Pico 2W 
2. **Setting up VS Code with MicroPico extension** for development

---

## Part 1: Install MicroPython on Your Pico 2W

### Download MicroPython
1. **Download the firmware**: Go to https://micropython.org/download/RPI_PICO2_W/
2. **Download the latest .uf2 file** (e.g., `RPI_PICO2_W-20241025-v1.24.0.uf2`)

### Flash the Firmware
1. **Hold the BOOTSEL button** while plugging in the Pico — it mounts as `RPI-RP2`
2. **Copy the downloaded .uf2 file** onto that drive
3. **Wait ~5 seconds**, then unplug and replug without BOOTSEL
4. It should now boot into MicroPython (not appear as RPI-RP2)

### How to Verify MicroPython Installation
**On macOS Terminal:**
```bash
ls /dev/tty.usb*
```
You should see something like `/dev/tty.usbmodem14201`

**On Linux Terminal:**
```bash
ls /dev/ttyACM*
```
You should see something like `/dev/ttyACM0`

**On Windows:**
- Open Device Manager → Ports (COM & LPT)
- Look for "USB Serial Device" (e.g., COM3)

## Part 2: Set Up VS Code with MicroPico Extension

### Install MicroPico Extension
1. **Open VS Code Extensions panel** (Ctrl/Cmd + Shift + X)
2. **Search for "MicroPico"**
3. **Install "MicroPico" by paulober** (`paulober.pico-w-go`)
4. **Important**: Make sure it's by "paulober" (not other MicroPython extensions)

### Test Your Setup
1. **Clone your lab repository** and open it in VS Code
2. **Connect your Pico 2W** via USB (normal connection, no BOOTSEL)
3. **Initialize MicroPico**: Press Ctrl/Cmd + Shift + P → "MicroPico: Initialize MicroPico"
4. **Test the LED**: Open `led_test.py` and run it using Ctrl/Cmd + Shift + P → "MicroPico: Run current file"
5. **Verify**: You should see the green LED on your Pico blink and terminal output

### Success Indicators
- ✅ Bottom status bar shows "MicroPico" with connection indicator
- ✅ `led_test.py` runs and LED blinks green
- ✅ Terminal shows LED control messages

### Troubleshooting
- **"Disconnected" in VS Code**: Try "MicroPico: Connect" from Command Palette
- **No LED blinking**: Make sure to use `Pin("LED", Pin.OUT)` for Pico 2W
- **Extension not working**: Verify you installed **MicroPico by paulober**
