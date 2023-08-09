import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def calculate_voltage():
    # Fetch data from Entry widgets
    V_nominal = float(voltage_entry.get())
    V_tolerance = float(voltage_tolerance_entry.get()) * V_nominal / 100
    R1_initial = float(r1_resistance_entry.get())
    R2_nominal = float(r2_resistance_entry.get())
    temp_coefficient_R1 = float(temp_coefficient_R1_entry.get()) * 1e-6  # ppm to per degree
    temp_coefficient_R2 = float(temp_coefficient_R2_entry.get()) * 1e-6  # ppm to per degree
    tolerance_R1 = float(tolerance_R1_entry.get()) / 100
    tolerance_R2 = float(tolerance_R2_entry.get()) / 100
    
    min_temperature = float(min_temperature_entry.get())
    max_temperature = float(max_temperature_entry.get())
    temperature_steps = int(temperature_steps_entry.get())

    temperature_values = np.linspace(min_temperature, max_temperature, temperature_steps)

    # Calculations
    voltage_min_values = []
    voltage_max_values = []
    for temperature in temperature_values:
        R1_min = R1_initial * (1 - tolerance_R1) * (1 + temp_coefficient_R1 * (temperature - 25))
        R1_max = R1_initial * (1 + tolerance_R1) * (1 + temp_coefficient_R1 * (temperature - 25))
        
        R2_min = R2_nominal * (1 - tolerance_R2) * (1 + temp_coefficient_R2 * (temperature - 25))
        R2_max = R2_nominal * (1 + tolerance_R2) * (1 + temp_coefficient_R2 * (temperature - 25))
        
        V_min = V_nominal * (1 - V_tolerance / V_nominal)
        V_max = V_nominal * (1 + V_tolerance / V_nominal)
        
        voltage_r2_min = V_min * (R2_min / (R1_max + R2_min))
        voltage_r2_max = V_max * (R2_max / (R1_min + R2_max))
        
        voltage_min_values.append(voltage_r2_min)
        voltage_max_values.append(voltage_r2_max)

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(temperature_values, voltage_min_values, label='Min Voltage')
    plt.plot(temperature_values, voltage_max_values, label='Max Voltage')
    plt.fill_between(temperature_values, voltage_min_values, voltage_max_values, color='yellow', alpha=0.3)
    plt.axvspan(21, 39, color='cyan', alpha=0.5, label="21°C - 39°C")
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Voltage across R2 (V)')
    plt.title('Voltage across R2 with Changing Temperature')
    plt.legend()
    plt.grid()

    plt.show()

# Create the main window
window = tk.Tk()
window.title("Voltage Across R2 Calculator")


entries = [
    ("Nominal Voltage (V):", '220'),
    ("Voltage Tolerance (%):", '10'),
    ("R1 Initial Resistance (Ohm):", '1.2e6'),
    ("R2 Nominal Resistance (Ohm):", '1.2e3'),
    ("Temperature Coefficient for R1 (ppm/°C):", '50'),
    ("Temperature Coefficient for R2 (ppm/°C):", '50'),
    ("Tolerance for R1 (%):", '1'),
    ("Tolerance for R2 (%):", '1'),
    ("Minimum Temperature (°C):", '-25'),
    ("Maximum Temperature (°C):", '120'),
    ("Temperature Steps:", '146')
]

# Load and display the image
image_path = "image.gif"  # Replace with your image's path
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(window, image=photo)
label_image.grid(column=4, row=0, rowspan=len(entries) + 25, padx=(0, 25))  # Added padx for padding on the right side.


for idx, (label_text, default_value) in enumerate(entries):
    ttk.Label(window, text=label_text).grid(column=0, row=idx, padx=20, pady=5)
    entry = ttk.Entry(window)
    entry.grid(column=2, row=idx)
    entry.insert(tk.END, default_value)

    if label_text.startswith("Temperature Coefficient for R1"):
        temp_coefficient_R1_entry = entry
    elif label_text.startswith("Temperature Coefficient for R2"):
        temp_coefficient_R2_entry = entry
    elif label_text.startswith("R1 Initial Resistance"):
        r1_resistance_entry = entry
    elif label_text.startswith("R2 Nominal Resistance"):
        r2_resistance_entry = entry
    elif label_text.startswith("Tolerance for R1"):
        tolerance_R1_entry = entry
    elif label_text.startswith("Tolerance for R2"):
        tolerance_R2_entry = entry
    elif label_text.startswith("Nominal Voltage"):
        voltage_entry = entry
    elif label_text.startswith("Voltage Tolerance"):
        voltage_tolerance_entry = entry
    elif label_text.startswith("Minimum Temperature"):
        min_temperature_entry = entry
    elif label_text.startswith("Maximum Temperature"):
        max_temperature_entry = entry
    elif label_text.startswith("Temperature Steps"):
        temperature_steps_entry = entry

calculate_button = ttk.Button(window, text="Calculate", command=calculate_voltage)
calculate_button.grid(column=1, row=len(entries), pady=20)

window.mainloop()
