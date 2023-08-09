# Voltage Across R2 Calculator

A graphical user interface (GUI) based tool to calculate the voltage across a resistor (R2) in a series circuit [voltage divider calculator], factoring in various tolerances and temperature coefficients. The tool leverages `tkinter` for the GUI and `matplotlib` for visualizing the data.

![Screenshot of the Application](screenshot.png)  <!-- If you have a screenshot, replace 'path_to_screenshot.png' with the actual path -->

## Features

- Calculate the minimum and maximum voltage across R2 with changing temperatures.
- Visual representation of voltage changes using `matplotlib`.
- Ability to input various parameters:
    - Nominal Voltage
    - Voltage Tolerance
    - Initial Resistance for R1 and R2
    - Temperature Coefficients for R1 and R2
    - Tolerances for R1 and R2
    - Temperature Range (Min and Max)
    - Temperature Steps for calculations

## Installation and Usage

1. **Clone the Repository** 
```bash
git clone https://github.com/your_username/voltage-calculator.git
```

2. **Navigate to the Directory**

```bash
cd voltage-calculator
```

3. **Run the Application**

```bash
python main.py  # Ensure that you have the required dependencies installed.
```

Dependencies
numpy
matplotlib
tkinter <!-- Included in the standard library for Python -->
To install the necessary libraries (except tkinter which is part of the Python standard library), you can use:




Contributions
Feel free to fork the repository and submit pull requests! All contributions are welcome.

License
This project is licensed under the MIT License. See the LICENSE file for details.