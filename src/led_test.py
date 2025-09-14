# Simple LED Test with Debug Output
from machine import Pin
import time

print("Starting LED test...")

# Try using "LED" pin identifier for Pico 2W
try:
    led = Pin("LED", Pin.OUT)
    print("✓ LED pin configured successfully using 'LED' identifier")
except:
    try:
        led = Pin(25, Pin.OUT)
        print("✓ LED pin configured successfully using pin 25")
    except Exception as e:
        print(f"✗ LED configuration failed: {e}")
        exit()

print("Testing LED control...")

for i in range(5):
    print(f"Attempt {i+1}: LED ON")
    led.on()
    print(f"  LED value after ON: {led.value()}")  # Should print 1
    time.sleep(1)
    
    print(f"Attempt {i+1}: LED OFF")
    led.off()
    print(f"  LED value after OFF: {led.value()}")  # Should print 0
    time.sleep(1)

print("Test complete!")
print("If LED values show 1/0 but no light, the LED might be:")
print("- Very dim or small")
print("- On the bottom of the board")
print("- Not present on this Pico variant")
