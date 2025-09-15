"""
Smart Light Controller - Lab 2
CMPSC 100: Cprint("\nCalculated Light Patterns:")
# TODO 3: Create and display calculations
# Calculate brightness_value by converting brightness_percent (0-100) to 0-255 scale
# Calculate pattern_duration = blink_cycles * blink_speed_seconds * 2
# Print both calculated values with labels
# Note: Brightness calculation is for learning - LED brightness doesn't actually change

print("\nPhysical LED Control:")
print("  Built-in LED Pin: \"LED\" (digital on/off)")

# TODO 4: Control the LED with conditionals
# Use if/else to control the LED based on led_state:
# if led_state is True: set led.on() and print status with brightness_percent
# if led_state is False: set led.off() and print status
# Note: brightness_percent is for learning - LED is digital on/off onlyxpression

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

# Set up the built-in LED for digital control
led = Pin("LED", Pin.OUT)

print("===============================================")
print("     SMART LIGHT CONTROLLER v2.0")
print("         Pico 2W IoT Device Setup")
print("===============================================")

print("\n🔧 LIGHT CONFIGURATION SETUP")
print("Let's configure your smart light controller!")

# TODO 1: Get light configuration from user
# Use input() to collect these values from the user:
# user_room_name = input("Enter your room name: ")
# brightness_percent = int(input("Enter brightness level (0-100): "))
# led_choice = input("Should LED start ON? (yes/no): ").lower()
# led_state = True if led_choice == "yes" else False
# blink_speed_seconds = float(input("Enter blink speed in seconds (e.g., 0.5): "))
# blink_cycles = int(input("Enter number of blink cycles (1-5): "))

# TODO 1a: After getting user input, display the personalized header
# print(f"\n===============================================")
# print(f"     SMART LIGHT CONTROLLER v2.0")
# print(f"         Pico 2W IoT Device - {user_room_name}")
# print(f"===============================================")

print("\nCurrent Light Settings:")
# TODO 2: Print your variable values
# Print each variable with a descriptive label

print("\nCalculated Light Patterns:")
# TODO 3: Create and display calculations
# Calculate: brightness_value = brightness_percent * 255 / 100
# Calculate: pattern_duration = blink_cycles * blink_speed_seconds * 2
# Print both calculated values with labels

print("\nPhysical LED Control:")
print("  Built-in LED Pin: \"LED\" (digital on/off)")

# TODO 4: Control the LED with conditionals
# Use if/else to control the LED based on led_state:
# if led_state is True: set led.on() and print status with brightness_percent
# if led_state is False: set led.off() and print status
# Note: brightness_percent is for learning - LED is digital on/off only

# TODO 5: Create simple blink pattern (no loops!)
# Use multiple if statements to create blinking:
# if blink_cycles >= 1: led.on(), sleep, led.off(), sleep
# if blink_cycles >= 2: led.on(), sleep, led.off(), sleep
# if blink_cycles >= 3: led.on(), sleep, led.off(), sleep
# if blink_cycles >= 4: led.on(), sleep, led.off(), sleep  
# if blink_cycles >= 5: led.on(), sleep, led.off(), sleep
# Return LED to configured state with: led.on() or led.off()

print("  Hardware Status: Ready")

print("\nSystem Performance:")
# TODO 6: Add performance status
# Create and print variables for:
# pattern_accuracy (str): accuracy percentage
# hardware_response (str): response quality

print("\n===============================================")
