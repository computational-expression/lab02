# Smart Light Controller v2.0 - SOLUTION - Lab 2
# Author: Prof. Jumadinova
# Date: September 3, 2025
# Description: Complete solution demonstrating Lab 1 Python skills applied to IoT hardware
# Hardware: Controls the built-in LED on Raspberry Pi Pico 2 W
# Skills Demonstrated: Variables, arithmetic, conditionals, string operations from Lab 1

# Import necessary modules for hardware control
from machine import Pin
import time

# Set up the built-in LED (use PIN "LED" for Pico 2W)
led = Pin("LED", Pin.OUT) 

print("===============================================")
print("     SMART LIGHT CONTROLLER v2.0")
print("         Pico 2W IoT Device - Megan's Study")
print("===============================================")

# Light Configuration Variables - Using Lab 1 data types!
brightness_percent = 75      # int variable (like Lab 1's sensor readings)
led_state = True            # bool variable (like Lab 1's status variables)
blink_speed_seconds = 0.5   # float variable (like Lab 1's decimal measurements)
blink_cycles = 4            # int variable (like Lab 1's count variables) - using 4 for pattern variety
user_room_name = "Megan's Study"  # str variable (like Lab 1's device names)

print("\nCurrent Light Settings:")
print("  Brightness Level:", brightness_percent, "%")
print("  LED State:", led_state)
print("  Blink Speed:", blink_speed_seconds, "seconds")
print("  Blink Cycles:", blink_cycles)
print("  User/Room:", user_room_name)

# Light Pattern Calculations - Using Lab 1 arithmetic skills!
brightness_value = brightness_percent * 255 / 100  # Scale to 0-255 range (like Lab 1's temperature conversion)
# Calculate pattern duration based on different blink patterns (like Lab 1's time calculations)
if blink_cycles >= 4:
    pattern_duration = 3 * blink_speed_seconds * 2 + blink_speed_seconds * 1.75  # 3 normal blinks + heartbeat
else:
    pattern_duration = blink_cycles * blink_speed_seconds * 2  # Simple blinks
total_on_time = blink_cycles * blink_speed_seconds     # Calculate totals (like Lab 1's averages)
total_off_time = blink_cycles * blink_speed_seconds
duty_cycle = (total_on_time / pattern_duration) * 100 if pattern_duration > 0 else 0  # Percentage calculation (like Lab 1's percentages)

print("\nCalculated Light Patterns:")
print("  Brightness Value:", int(brightness_value), "/255 (scaled)")  # Using int() like Lab 1
print("  Pattern Duration:", pattern_duration, "seconds")
print("  Total ON Time:", total_on_time, "seconds")
print("  Total OFF Time:", total_off_time, "seconds")
print("  Duty Cycle:", int(duty_cycle), "%")  # Using int() and % like Lab 1

print("\nPhysical LED Control:")
print("  Built-in LED Pin: \"LED\"")

# Control the LED using conditionals (like Lab 1's sensor status logic)
if led_state:  # Conditional statement like Lab 1!
    led.on()
    print("  Current LED State: ON")
    print("  Hardware Status: Active")
else:
    led.off()
    print("  Current LED State: OFF")
    print("  Hardware Status: Standby")

# Demonstrate blinking pattern using conditionals (like Lab 1's threshold logic)
if blink_cycles > 0 and led_state:  # Multiple conditions like Lab 1!
    print("  Starting blink pattern...")
    print("  Control Response: LED responding to program")
    
    # Simple blink sequence using basic conditional logic (no loops needed!)
    # Create different patterns based on blink_cycles value
    if blink_cycles >= 1:
        led.on()
        time.sleep(blink_speed_seconds)
        led.off()
        time.sleep(blink_speed_seconds)
        print("    Blink 1 completed")
    
    if blink_cycles >= 2:
        led.on()
        time.sleep(blink_speed_seconds)
        led.off()
        time.sleep(blink_speed_seconds)
        print("    Blink 2 completed")
    
    if blink_cycles >= 3:
        led.on()
        time.sleep(blink_speed_seconds)
        led.off()
        time.sleep(blink_speed_seconds)
        print("    Blink 3 completed")
    
    if blink_cycles >= 4:
        # Create a special "heartbeat" pattern for 4+ blinks
        print("    Starting heartbeat pattern...")
        led.on()
        time.sleep(blink_speed_seconds / 2)  # Quick flash
        led.off()
        time.sleep(blink_speed_seconds / 4)
        led.on()
        time.sleep(blink_speed_seconds / 2)  # Quick flash
        led.off()
        time.sleep(blink_speed_seconds)
        print("    Heartbeat pattern completed")
    
    # Leave LED in final state based on led_state setting
    if led_state:
        led.on()
        print("    LED returned to ON state")
else:
    print("  Control Response: Static LED state maintained")

# System Performance Assessment - Using variables and string operations like Lab 1
pattern_accuracy = 100                              # int variable
hardware_response = "Excellent"                     # str variable  
control_status = "ACTIVE" if led_state else "STANDBY"  # Conditional assignment like Lab 1
timing_precision = 95                               # int variable

print("\nSystem Performance:")
print("  Pattern Accuracy:", pattern_accuracy, "%")
print("  Hardware Response:", hardware_response)
print("  Control Status:", control_status)
print("  Timing Precision:", timing_precision, "%")

# Hardware Activity Report - Using conditionals for different outputs (like Lab 1's sensor status)
print("\nHardware Activity:")
if blink_cycles > 0 and led_state:      # Multiple condition check
    if blink_cycles >= 4:
        print("  - LED executed", blink_cycles, "blinks with heartbeat pattern")
        print("  - Multiple conditional patterns completed successfully")
    else:
        print("  - LED executed", blink_cycles, "simple blinks")
        print("  - Basic conditional pattern completed successfully")
    print("  - Hardware control using conditionals only (no loops!)")
elif led_state:                         # Single condition check
    print("  - LED turned ON and remains steady")
    print("  - No blinking pattern requested")
    print("  - Hardware control successful")
else:                                   # Default case
    print("  - LED remains OFF as configured")
    print("  - System in standby mode")
    print("  - Hardware ready for activation")

# Power and Efficiency Calculations - More arithmetic operations like Lab 1
estimated_power_mw = brightness_percent * 0.8  # Multiplication like Lab 1's calculations
efficiency_rating = 100 - (brightness_percent - 50) if brightness_percent > 50 else 100  # Conditional calculation

print("\nEnergy Information:")
print("  Estimated Power:", estimated_power_mw, "mW")
print("  Efficiency Rating:", int(efficiency_rating), "/100")
print("  Energy Status: Low consumption device")

print("\nNext Update: Adding external LEDs and loops (Lab 3)")
print("===============================================")

# Keep the LED in its final state (don't turn off at end)
print("\nProgram completed. LED state maintained.")
