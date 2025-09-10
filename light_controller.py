# Smart Light Controller v2.0 - Lab 2
# Author: [Your Name Here]
# Date: [Today's Date]
# Description: Apply Lab 1 Python skills to control actual Pico 2W hardware
# Hardware: Controls the built-in LED on Raspberry Pi Pico 2 W
# Skills: Variables, arithmetic, conditionals, string operations from Lab 1

# Import necessary modules for hardware control
from machine import Pin
import time

# Set up the built-in LED (connected to GPIO pin 25)
led = Pin(25, Pin.OUT)

print("===============================================")
print("     SMART LIGHT CONTROLLER v2.0")
print("         Pico 2W IoT Device - [Your Room Name]")
print("===============================================")

# *** LAB 2: APPLYING LAB 1 SKILLS TO HARDWARE! ***
# This lab uses the same Python concepts from Lab 1:
# - Variables (int, float, str, bool) to store light settings
# - Arithmetic operations to calculate light patterns  
# - Conditionals (if/else) to control LED behavior
# - String operations for professional output
# The difference: Now we control REAL HARDWARE!

# TODO: Light Configuration Variables - Apply Lab 1 variable skills!
# Create variables for light settings using the same data types from Lab 1:
# int variables for counts and percentages
# float variables for timing measurements  
# str variables for names and status
# bool variables for on/off states
brightness_percent = 0      # Replace with brightness level (0-100) - int variable like Lab 1
led_state = False          # Replace with True for ON, False for OFF - bool variable like Lab 1  
blink_speed_seconds = 0.0   # Replace with blink speed in seconds - float variable like Lab 1
blink_cycles = 0            # Replace with number of blinks - int variable like Lab 1
user_room_name = "Replace with your name or room name"  # str variable like Lab 1

print("\nCurrent Light Settings:")
print("  Brightness Level:", brightness_percent, "%")
print("  LED State:", led_state)
print("  Blink Speed:", blink_speed_seconds, "seconds")
print("  Blink Cycles:", blink_cycles)
print("  User/Room:", user_room_name)

# TODO: Light Pattern Calculations - Apply Lab 1 arithmetic skills!
# Add calculations similar to Lab 1's sensor analysis:
# Example: brightness_value = brightness_percent * 255 / 100  (like Lab 1's temperature conversion)
# Example: pattern_duration = blink_cycles * blink_speed_seconds * 2  (like Lab 1's time calculations)

print("\nCalculated Light Patterns:")
# TODO: Add your calculated values with print statements
# Example: print("  Brightness Value:", brightness_value, "/255 (scaled)")
# Example: print("  Pattern Duration:", pattern_duration, "seconds")

# TODO: Hardware LED Control - Apply Lab 1 conditional skills!
# Control the actual LED using conditionals from Lab 1:
print("\nPhysical LED Control:")
print("  Built-in LED Pin: 25")

# Example LED control using conditionals (like Lab 1's sensor status logic):
# if led_state:  # This is a conditional statement like Lab 1!
#     led.on()
#     print("  Current LED State: ON")
# else:
#     led.off()
#     print("  Current LED State: OFF")

# TODO: Add simple LED pattern using conditionals (no loops needed!)
# Note: We use multiple if statements instead of loops to keep focus on Lab 1 skills
# Loops will be introduced in Lab 3!
# Example simple blinking with conditional:
# if blink_cycles >= 1:  # Conditional logic like Lab 1!
#     print("  Starting simple blink pattern...")
#     # Simple blink sequence (no loop needed)
#     led.on()
#     time.sleep(blink_speed_seconds)
#     led.off()
#     time.sleep(blink_speed_seconds)
#     print("    Blink 1 completed")
# if blink_cycles >= 2:
#     led.on()
#     time.sleep(blink_speed_seconds)
#     led.off()
#     time.sleep(blink_speed_seconds)
#     print("    Blink 2 completed")

print("  Hardware Status: Ready")
print("  Control Response: LED ready for commands")

print("\nSystem Performance:")
# TODO: Add your performance assessment variables with print statements
# Example: print("  Pattern Accuracy: 100%")
# Example: print("  Hardware Response: Excellent")

print("\nHardware Activity:")
print("  - Add descriptions of LED behavior here")
print("  - Include information about blinking patterns")
print("  - Report on hardware control success")

print("\nNext Update: Adding external LEDs and loops (Lab 3)")
print("===============================================")
