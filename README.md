# Lab 2: IoT Hardware Introduction - Smart Light Controller
**CMPSC 100: Computational Expression Fall 2025**

## Meet Your Raspberry Pi Pico 2 W

The **Raspberry Pi Pico 2 W** is a powerful microcontroller that brings the physical world into your programming experience. Unlike a regular computer, this tiny board is designed to interact directly with electronic components like LEDs, sensors, and motors.

### How the Pico 2 W Works

The Pico 2 W operates on **3.3 volts** of electricity and contains:
- **GPIO pins** (General Purpose Input/Output) that can send electrical signals to control LEDs or read sensor data
- A **wireless chip** for WiFi connectivity, enabling true IoT functionality
- **Flash memory** to store your Python programs permanently
- A **dual-core processor** running at 150MHz to execute your code

When you write code to control an LED, you're actually telling the Pico to send a **3.3V electrical signal** through specific pins. LEDs (Light Emitting Diodes) work by allowing current to flow in one direction, converting electrical energy into light. The built-in LED on your Pico 2W can be controlled using the `"LED"` pin identifier through MicroPython commands.

This direct hardware control is what makes microcontrollers different from regular computers - your code immediately affects the physical world through electricity and electronic components.

## Overview

Welcome to your introduction to physical computing and IoT hardware! In Lab 1, you mastered Python fundamentals including variables, data types, arithmetic operations, string manipulation, input/output, and basic conditionals using a sensor simulation. Now in Lab 2, you'll apply those same programming concepts, with the addition of conditionals, to control actual hardware with the Raspberry Pi Pico 2 W.

This lab transitions you from simulation to reality by introducing you to the hardware, development environment, and MicroPython programming. You will create a **Smart Light Controller** that actually controls the built-in LED on your Pico 2 W and displays system information using the Python skills you've already learned.

By the end of this lab, you will have a working physical light controller that responds to your programming - bridging the gap between the software concepts from Lab 1 and the IoT systems you'll build throughout the semester.

## Learning Objectives

By completing this lab, you will be able to:

1. **Set up the MicroPython development environment** in VS Code for physical IoT hardware control
2. **Apply Python programming fundamentals** from Lab 1 (variables, data types, arithmetic, conditionals) to control physical hardware
3. **Control actual hardware** by turning the Pico's built-in LED on and off through code
4. **Create structured output** using the print statement and string formatting skills from Lab 1
5. **Use basic conditionals** to control LED behavior based on program variables
6. **Bridge the gap** between software simulation (Lab 1) and physical IoT systems

### Alignment with Course Learning Outcomes

This lab directly supports the following course learning outcomes:

- **LO1**: Apply Python programming fundamentals to execute and explain computer code that implements interactive, novel solutions to a variety of computable problems.
- **LO2**: Implement code consistent with industry-standard practices using professional-grade integrated development environments (IDEs), command-line tools, and version control systems.

### Distribution Requirements Alignment

- **Modes of Expression (ME)**: You will express computational ideas through Python code and written reflections
- **Scientific Process (SP)**: You will apply systematic reasoning to solve problems and analyze your results

## Prerequisites

Before starting this lab, ensure you have:
- Completed Lab 1 (Digital Sensor Simulation Dashboard) - understanding of Python variables, data types, arithmetic operations, string manipulation, and basic conditionals
- VS Code installed and configured
- Git set up for version control
- Your Pico 2 W board and USB cable with **MicroPython already installed** (see `PICO_SETUP.md` if needed)

## Getting Started

### Step 1: Clone and Open Repository
1. **Clone this repository** to your local machine:
   ```bash
   git clone [repository-url]
   cd lab02
   ```
2. **Open in VS Code**:
   ```bash
   code .
   ```

### Step 2: Install MicroPico Extension (One-Time Setup)
**If this is your first Pico lab:**
1. **Open Extensions panel** (Ctrl/Cmd + Shift + X)
2. **Search for "MicroPico"** and install **"MicroPico" by paulober**
3. **Extension ID**: `paulober.pico-w-go`

### Step 3: Connect and Test Your Pico
1. **Connect your Pico 2 W** via USB (normal connection)
2. **Initialize project**: Press Ctrl/Cmd + Shift + P → "MicroPico: Initialize MicroPico"
3. **Test the LED**: Open `led_test.py` and run it (Ctrl/Cmd + Shift + P → "MicroPico: Run current file")
4. **Verify**: Green LED should blink and you should see terminal output

**✅ Success**: You should see "MicroPico" in the bottom status bar and a blinking green LED!

## Start Coding: Your First Hardware Program

**From Lab 1 to Lab 2**: In Lab 1, you used `print()` to display sensor simulation results. Now in Lab 2, you'll use the same programming concepts to control actual hardware!

**Ready to code?** Open `light_controller.py` and start applying your Lab 1 Python skills to control real hardware!

## The Lab Challenge: Smart Light Controller v2.0

**Building on Lab 1:** In Lab 1, you simulated sensor data using Python variables, calculations, and conditionals. Now you'll use those same programming concepts to control actual hardware!

**Important File Organization:**
- Keep all your code files in the GitHub repository folder you cloned
- The `light_controller.py` file is already provided as a starter
- Your work stays in your local repo and gets committed/pushed to GitHub
- The MicroPico extension runs files directly from your repo folder on the Pico

### Phase 1: Development Environment Setup (20 minutes)
*Complete this during the in-class session*

**Your environment should now be ready from the Getting Started steps above. Let's verify:**

1. **Open `light_controller.py`** from your repository folder
2. **Make sure your Pico 2 W is connected** and VS Code shows "MicroPico" in the status bar
3. **Test with `led_test.py`**: Run it to verify the green LED blinks

## 💡 Troubleshooting

**LED not working?** 
- Make sure you use `Pin("LED", Pin.OUT)` (not Pin 25)
- Run `led_test.py` to verify your Pico LED works
- Look for the green LED on your Pico 2W board

**Connection issues?**
- Open Command Palette (`Ctrl+Shift+P`) → "MicroPico: Connect"
- Try "MicroPico: Disconnect" then "MicroPico: Connect"
- Make sure you installed **MicroPico by paulober**

**Need detailed setup help?** See `PICO_SETUP.md` for complete hardware and software setup instructions.

---

### How to Run Your Code

**Simple Steps:**
1. **Open** your `light_controller.py` file in VS Code
2. **Press** `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open Command Palette
3. **Type** "MicroPico: Run current file" and select it
4. **Watch** the output in VS Code terminal AND the LED on your Pico!

**Alternative**: Click the ▶ button in the top-right corner when viewing .py files

**Your code files stay in your GitHub repository folder** - the MicroPico extension runs them directly on the Pico.

### Phase 2: Smart Light Control with Python Fundamentals (45 minutes)
*Begin in class, complete outside of class*

You will build a Smart Light Controller that applies the Python concepts from Lab 1 to control physical hardware. Your system needs to demonstrate:

**Lab 1 Skills Applied to Hardware:**

1. **Variables and Data Types**: Use the same variable types from Lab 1 to store light settings:
   - `int` variables for brightness levels and blink counts  
   - `float` variables for timing measurements
   - `str` variables for user/room names and status messages
   - `bool` variables for LED state (True/False)

2. **Arithmetic Operations**: Use calculations similar to Lab 1's sensor analysis:
   - Convert brightness percentage to practical values (like Lab 1's temperature conversion)
   - Calculate total blink cycles and timing (like Lab 1's time calculations)
   - Determine timing intervals and performance metrics (like Lab 1's averages)

3. **String Operations**: Apply Lab 1's string skills for hardware status:
   - String concatenation for device IDs and status messages
   - `.upper()` method for professional status displays (like Lab 1)
   - String formatting for hardware reports

4. **Conditionals**: Use `if` statements to control hardware based on variables:
   - `if led_state:` to turn LED on or off
   - `if blink_cycles >= 1:` to create simple blink patterns
   - Multiple `if` statements to create different LED behaviors
   - Conditional logic for system status determination (no loops needed!)

**Note**: This lab intentionally uses only conditionals and basic statements (no loops) to keep the focus on applying Lab 1 skills to hardware. Loops will be introduced in Lab 3!

**Physical Hardware Control**: Your program will actually turn the built-in LED on and off, demonstrating how Lab 1's programming concepts control real hardware!

### Phase 3: System Documentation and Testing (25 minutes)
*Complete outside of class*

1. **Code Documentation**: Add comprehensive comments explaining:
   - Purpose of each variable and calculation
   - How the environmental assessments work
   - What each section of output represents

2. **Data Validation**: Create additional variables to:
   - Check if readings are within realistic ranges
   - Calculate data quality indicators
   - Show system confidence levels

3. **Testing Different Scenarios**: Modify your light settings to test:
   - Different brightness levels and see the LED respond
   - Various blink speeds and patterns
   - Different numbers of blink cycles
   - Watch how changing variables affects the physical LED behavior

**Important**: You are now controlling actual hardware! The built-in LED on your Pico will physically turn on and off based on your program settings.

**Example Output Format:**
```
===============================================
     SMART LIGHT CONTROLLER v2.0
         Pico 2W IoT Device - Alex's Room
===============================================

Current Light Settings:
  Brightness Level: 75%
  LED State: ON
  Blink Speed: 0.5 seconds
  Blink Cycles: 4
  User/Room: Alex's Room

Calculated Light Patterns:
  Brightness Value: 191/255 (scaled)
  Pattern Duration: 3.9 seconds
  Total ON Time: 2.0 seconds
  Total OFF Time: 2.0 seconds
  
Physical LED Control:
  Built-in LED Pin: "LED"
  Current LED State: ON
  Hardware Status: Active
  Control Response: LED responding to program
  
System Performance:
  Pattern Accuracy: 100%
  Hardware Response: Excellent
  Control Status: ACTIVE
  Timing Precision: 95%

Hardware Activity:
  - LED physically blinking in patterns
  - Multiple conditional behaviors active
  - Hardware control successful using conditionals

Next Update: Adding external LEDs and loops (Lab 3)
===============================================
```

## Assessment

This lab will be evaluated based on the following criteria:

### Smart Light Controller Functionality (60%)
- **System Setup**: MicroPython environment properly configured and working with hardware
- **Python Fundamentals Applied**: Proper use of variables, data types, arithmetic operations, and conditionals from Lab 1
- **Hardware LED Control**: Built-in LED successfully controlled through code (on/off/blinking using conditionals)
- **Light Pattern Processing**: All required calculations implemented using arithmetic operations from Lab 1
- **String Operations**: Professional use of string concatenation, `.upper()` method, and formatting
- **Output Display**: Professional-looking formatted report using print statements and string skills from Lab 1
- **Code Execution**: Program runs without errors on the Pico 2 W and physically controls the LED
- **Requirements Compliance**: All specified light settings, calculations, and hardware control included

### Code Quality and IoT Design (25%)
- **Comments and Documentation**: Clear explanations of hardware control, light calculations, and system purpose
- **Variable Names**: Descriptive, professional naming following IoT development standards
- **Code Organization**: Logical structure that will support future IoT system expansion
- **Hardware Integration**: Proper use of MicroPython modules for LED control
- **Output Formatting**: Professional appearance suitable for real smart home devices

### System Foundation and Reflection (15%)
- **IoT Context Understanding**: Demonstrates understanding of how this fits into larger IoT system
- **README Documentation**: Updated with system description and future development plans
- **Testing and Validation**: Evidence of testing different environmental scenarios
- **Reflection**: Thoughtful analysis of learning and connection to IoT development

### Submission Requirements

1. **Complete Smart Light Controller Program**:
   - `light_controller.py` - Your main program file

2. **Updated Documentation**:
   - README.md with system description and reflection
   - Brief explanation of how this foundation will support future IoT features
   - Description of the light control scenarios you tested

3. **Version Control**:
   - Commit your work to Git with meaningful commit messages
   - Push to your repository

4. **System Testing**:
   - Test your program on the Pico 2 W using one of the methods above
   - Verify the built-in LED responds to your code
   - Try different light settings to ensure calculations work
   - Observe the physical LED blinking patterns

**Quick Testing Steps:**
1. Connect your Pico 2 W via USB
2. Open `light_controller.py` in VS Code
3. Press **Ctrl+Shift+P** and select "MicroPico: Run current file"
4. Watch the terminal output AND the LED on your Pico
5. Modify variables in your code and run again to see different behaviors

## Looking Ahead: Building Your IoT System

This lab bridges Lab 1's Python fundamentals with physical computing, preparing you for the complete IoT system you will build:

- **Lab 1 (Completed)**: Python fundamentals with sensor simulation - variables, arithmetic, strings, conditionals
- **Lab 2 (This Lab)**: Apply Lab 1 skills to control actual hardware - Pico setup and basic LED control  
- **Lab 3 (Week 4)**: Add external LEDs and more complex patterns using loops and functions
- **Lab 4 (Week 5)**: Create modular functions for different lighting operations
- **Lab 5 (Week 6)**: Add user interaction and preference logging
- **Lab 6 (Week 7)**: Implement smart responses based on usage patterns
- **Lab 7 (Week 9)**: Advanced testing and debugging techniques
- **Labs 8-10 (Weeks 10-12)**: Add environmental sensing, object-oriented design, and full smart home integration

Each lab builds directly on the previous work, gradually evolving from Lab 1's simulation to a sophisticated smart home IoT system by the end of the semester.

## Getting Help

- **Technical Issues**: Use Discord or visit office hours for setup and coding problems
- **Conceptual Questions**: Review Week 2 class materials or ask during lab sessions
- **IoT System Design**: Discuss your smart light control approach with instructors
- **Debugging**: Use print statements to trace through your calculations step by step

## Reflection Questions

After completing the lab, consider these questions for your reflection:

1. How did applying Lab 1's Python concepts (variables, arithmetic, conditionals) to control physical hardware change your understanding of programming?
2. What was the most challenging part of transitioning from software simulation (Lab 1) to hardware control (Lab 2)?
3. How did using conditionals (`if` statements) to control the LED compare to using them for sensor status in Lab 1?
4. What similarities did you notice between Lab 1's sensor calculations and Lab 2's light pattern calculations?
5. How do you think the combination of Lab 1's Python skills and Lab 2's hardware control will prepare you for more complex IoT systems?

---

**Due Date**: [Insert due date here]  
**Points**: 4.5 points  
**Estimated Time**: 3-4 hours (1.5 hours in class, 1.5-2.5 hours outside class)  
**IoT System Progress**: Lab 1 Complete ✓ | Hardware Introduction Complete ✓
