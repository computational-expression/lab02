# Lab 2: IoT Hardware Introduction - Smart Light Controller

In this lab, you will apply Python fundamentals (variables, data types, arithmetic, conditionals) to control actual hardware with the Raspberry Pi Pico 2 W. Specifically, you will create a **Smart Light Controller** that controls the built-in LED on your Pico 2 W and displays system information using your Python programming skills.

## Meet Your Raspberry Pi Pico 2 W

The **Raspberry Pi Pico 2 W** is a powerful microcontroller that brings the physical world into your programming experience. Unlike a regular computer, this tiny board is designed to interact directly with electronic components like LEDs, sensors, and motors.

### How the Pico 2 W Works

The Pico 2 W operates on **3.3 volts** of electricity and contains:
- **GPIO pins** (General Purpose Input/Output) that can send electrical signals to control LEDs or read sensor data
- A **wireless chip** for WiFi connectivity, enabling true IoT functionality
- **Flash memory** to store your Python programs permanently
- A **dual-core processor** running at 150MHz to execute your code

When you write code to control an LED, you are actually telling the Pico to send a **3.3V electrical signal** through specific pins. LEDs (Light Emitting Diodes) work by allowing current to flow in one direction, converting electrical energy into light. The built-in LED on your Pico 2W can be controlled using the `"LED"` pin identifier through MicroPython commands.

This direct hardware control is what makes microcontrollers different from regular computers - your code immediately affects the physical world through electricity and electronic components.

## Learning Objectives

By completing this lab, you will be able to:

1. **Set up the MicroPython development environment** in VS Code for IoT hardware control
2. **Apply Python programming fundamentals** (variables, data types, arithmetic, conditionals) to control physical hardware
3. **Control actual hardware** by turning the Pico's built-in LED on and off through code
4. **Create structured output** using print statements and string formatting
5. **Use conditionals** to control LED behavior based on program variables

## Prerequisites

Before starting this lab, ensure you have:
- VS Code installed and configured
- Git set up for version control
- Your Pico 2 W board and USB cable with **MicroPython already installed**

## Getting Started

### Step 1: Clone and Open Repository
1. **Clone this repository** to your local machine:
   ```bash
   git clone [repository-url]
   cd lab02
   ```
2. **Open the repository directory in VS Code**

### Step 2: Install MicroPico Extension (One-Time Setup)
1. **Open Extensions panel** (Ctrl/Cmd + Shift + X)
2. **Search for "MicroPico"** and install **"MicroPico" by paulober**
3. **Extension ID**: `paulober.pico-w-go`

### Step 3: Connect and Test Your Pico
1. **Connect your Pico 2 W** via USB (normal connection)
2. **Initialize project**: Press Ctrl/Cmd + Shift + P → "MicroPico: Initialize MicroPico"
3. **Test the LED**: Open `src/led_test.py` and run it (Ctrl/Cmd + Shift + P → "MicroPico: Run current file")
4. **Verify**: Green LED should blink and you should see terminal output

**✅ Success**: You should see "MicroPico" in the bottom status bar and a blinking green LED!

## The Lab Challenge: Smart Light Controller

You will use Python programming concepts to control actual hardware.

**Your Tasks:**
- Edit `src/light_controller.py` to complete the smart light controller
- Write your reflection in `writing/reflection.md`

### Setup Verification

1. **Open `src/light_controller.py`** from your repository folder
2. **Make sure your Pico 2 W is connected** and VS Code shows "MicroPico" in the status bar
3. **Test with `src/led_test.py`**: Run it to verify the green LED blinks

**If you need help with Pico setup**, ask a TL or see [pico_setup instructions](https://github.com/computational-expression/pico_setup).

### How to Run Your Code

**Simple Steps:**
1. **Open** your `src/light_controller.py` file in VS Code
2. **Press** `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open Command Palette
3. **Type** "MicroPico: Run current file" and select it
4. **Watch** the output in VS Code terminal AND the LED on your Pico!

**Alternative**: Click the ▶ button in the top-right corner when viewing .py files

### Programming Requirements

You will build a Smart Light Controller that demonstrates:

1. **Variables and Data Types**: Store light settings using:
   - `int` variables for brightness levels and blink counts  
   - `float` variables for timing measurements
   - `str` variables for user/room names and status messages
   - `bool` variables for LED state (True/False)

2. **Arithmetic Operations**: Use calculations for:
   - Convert brightness percentage to practical values
   - Calculate total blink cycles and timing
   - Determine timing intervals and performance metrics

3. **String Operations**: Create professional output with:
   - String concatenation for device IDs and status messages
   - `.upper()` method for status displays
   - String formatting for hardware reports

4. **Conditionals**: Use `if` statements to control hardware:
   - `if led_state:` to turn LED on or off
   - `if blink_cycles >= 1:` to create simple blink patterns
   - Multiple `if` statements for different LED behaviors

**Note**: This lab uses only conditionals and basic statements (no loops) to focus on fundamental programming concepts we have been covering in class.

### Expected Output

Your program should produce professional output similar to this:
```
===============================================
     SMART LIGHT CONTROLLER v2.0
         Pico 2W IoT Device - Jasmine's Room
===============================================

Current Light Settings:
  Brightness Level: 75%
  LED State: ON
  Blink Speed: 0.5 seconds
  Blink Cycles: 4
  User/Room: Jasmine's Room

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

===============================================
```

## Assessment Criteria - Total: 4.5 Points

### Technical Implementation (3.0 points)

**Grading is based on GatorGrade automated checks:**
- **24 automated checks = 2.0 points**
- **Manual code review = 1.0 point** (hardware execution verification during lab session)
  - Program runs without errors on Pico 2W (0.5 points)
  - LED control functions correctly (on/off/blink) (0.5 points)
- **Partial credit:** Automated score = (checks passed ÷ 24) × 2.0 points

*The automated checks verify all technical requirements including:*
- *Program structure and completion (file exists, TODOs completed, comments)*
- *Hardware control setup (MicroPython imports, LED pin configuration)*
- *Variable assignments (all 5 required variables with appropriate types)*
- *Calculations and logic (arithmetic operations, conditionals for LED control)*
- *Reflection and documentation (reflection file completed)*
- *Test file verification (test file exists with LED control methods)*

### Code Quality and Style (1.0 point)  
- **Descriptive variable names** for hardware control (0.3 pts)
- **Clean, readable code organization** (0.3 pts)
- **Appropriate comments** explaining hardware logic (0.4 pts)

### Reflection and Engagement (0.5 points)
- **Thoughtful reflection** on learning and IoT hardware concepts

## Code Review (Separate Grading Component)

**This is a separate grading component: 2.2 points per code review. Not part of the 4.5-point lab grade. See the syllabus for more details.**

### Topics You May Need to Explain:
- **Variable types and naming conventions** for hardware control (Python programming concepts)
- **Arithmetic operations** used in LED calculations like brightness scaling, timing (Python programming concepts) 
- **Conditional statements** for LED control logic and hardware behavior (Python programming concepts)
- **Hardware control concepts** like pin configuration and MicroPython basics
- **Program logic** and flow for IoT hardware control and LED patterns

## Submission Instructions

Submit to GitHub frequently! The version submitted last before the due date will be the one that is graded. 

### Git Workflow

```bash
# Add your completed files (can also use `git add .`)
git add src/light_controller.py writing/reflection.md
```

```bash
# Commit with a descriptive message
git commit -m "Complete smart light controller with LED hardware control"
```

```bash
# Push to GitHub
git push
```

### Verification
- Go to your GitHub repository online
- Verify your files show your latest changes
- Check that GatorGrade passes (automated testing will run)
- **Test your program on Pico 2W**: Ensure LED responds correctly to your code

## Getting Help

### During Lab
- Ask TLs or instructor for help with specific questions or hardware issues
- Work with classmates on understanding concepts (but write your own code)
- Use the lab time to understand the hardware setup and get started with your program

### Outside Lab  
- Post questions in Discord
- Attend [TL office hours](https://www.cis.allegheny.edu/teaching/technicalleaders/) and/or [instructor office hours](https://janyljumadinova.com/schedule/) to seek help outside of class
- Review the slides for concept reinforcement

### Resources
- [Python Documentation](https://docs.python.org/3/)
- [MicroPython Documentation](https://docs.micropython.org/)
- Course slides: [Python Basics](https://computational-expression.github.io/course_information/week02/python_basics.html), [Types & Operations](https://computational-expression.github.io/course_information/week03/types_operations.html), [Conditionals](https://computational-expression.github.io/course_information/week03/conditionals.html)
- [Pico Setup Instructions](https://github.com/computational-expression/pico_setup)
- Examples from class activities
