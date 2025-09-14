"""
Smart Light Controller - Lab 2
CMPSC 100: Computational Expression

This program controls the built-in LED on a Raspberry Pi Pico 2W using Python fundamentals:
- Variables (int, float, str, bool) to store light settings
- Arithmetic operations to calculate light patterns  
- Conditionals (if/else) to control LED behavior
- String operations for professional output

Your task: Complete the TODOs below to create a working smart light controller.
"""

# Import necessary modules for hardware control
from machine import Pin
import time

# Set up the built-in LED
led = Pin("LED", Pin.OUT)

print("===============================================")
print("     SMART LIGHT CONTROLLER v2.0")
print("         Pico 2W IoT Device - [Your Room Name]")
print("===============================================")

# TODO 1: Create your light configuration variables
# Create these variables with meaningful values:
# brightness_percent (int): brightness level 0-100
# led_state (bool): True for ON, False for OFF  
# blink_speed_seconds (float): time between blinks
# blink_cycles (int): number of times to blink
# user_room_name (str): your name or room name

print("\nCurrent Light Settings:")
# TODO 2: Print your variable values
# Print each variable with a descriptive label

print("\nCalculated Light Patterns:")
# TODO 3: Create and display calculations
# Calculate: brightness_value = brightness_percent * 255 / 100
# Calculate: pattern_duration = blink_cycles * blink_speed_seconds * 2
# Print both calculated values with labels

print("\nPhysical LED Control:")
print("  Built-in LED Pin: \"LED\"")

# TODO 4: Control the LED with conditionals
# Use if/else to control the LED based on led_state:
# if led_state is True: turn LED on and print status
# if led_state is False: turn LED off and print status

# TODO 5: Create simple blink pattern (no loops!)
# Use multiple if statements to create blinking:
# if blink_cycles >= 1: blink once
# if blink_cycles >= 2: blink twice
# etc.

print("  Hardware Status: Ready")

print("\nSystem Performance:")
# TODO 6: Add performance status
# Create and print variables for:
# pattern_accuracy (str): accuracy percentage
# hardware_response (str): response quality

print("\n===============================================")
