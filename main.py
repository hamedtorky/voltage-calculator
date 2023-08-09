import numpy as np
import matplotlib.pyplot as plt

# Given parameters
nominal_voltage = 12  # Nominal voltage (V)
voltage_tolerance = 0.02 * nominal_voltage  # tolerance

R1_initial_resistance = 39e3  # Initial resistance of R1 (ohms)
R2_nominal_resistance = 12.4e3  # Nominal resistance of R2 (ohms)

R1_tolerance_percentage = 1.0  # Fixed tolerance of 1%
R2_tolerance_percentage = 1.0  # Assuming the same tolerance for R2 as R1 for simplicity

R1_temperature_coefficient = 100e-6  # Temperature coefficient (50 ppm/°C)
R2_temperature_coefficient = 100e-6  # Temperature coefficient (50 ppm/°C)
temperature_reference = 25  # Reference temperature (°C)

temperature_values = np.linspace(-25, 120, 146)  # Temperature range from -25°C to 120°C

temperature_bandwidth_start = 20
temperature_bandwidth_end = 45


# Initialize lists to store voltage data
voltage_min_values = []
voltage_max_values = []

for temperature in temperature_values:
    # Adjust resistance values based on temperature for R1
    R1_temp_adjusted_min = R1_initial_resistance * (1 - R1_tolerance_percentage / 100) * (1 + R1_temperature_coefficient * (temperature - temperature_reference))
    R1_temp_adjusted_max = R1_initial_resistance * (1 + R1_tolerance_percentage / 100) * (1 + R1_temperature_coefficient * (temperature - temperature_reference))
    
    # Adjust resistance values based on temperature for R2
    R2_temp_adjusted = R2_nominal_resistance * (1 + R2_temperature_coefficient * (temperature - temperature_reference))
    R2_temp_adjusted_min = R2_temp_adjusted * (1 - R2_tolerance_percentage / 100)
    R2_temp_adjusted_max = R2_temp_adjusted * (1 + R2_tolerance_percentage / 100)
    
    # Calculate minimum and maximum voltage across R2
    voltage_min = nominal_voltage * (1 - voltage_tolerance / 100)
    voltage_max = nominal_voltage * (1 + voltage_tolerance / 100)
    
    voltage_r2_min = voltage_min * (R2_temp_adjusted_min / (R1_temp_adjusted_max + R2_temp_adjusted_min))
    voltage_r2_max = voltage_max * (R2_temp_adjusted_max / (R1_temp_adjusted_min + R2_temp_adjusted_max))
    
    voltage_min_values.append(voltage_r2_min)
    voltage_max_values.append(voltage_r2_max)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(temperature_values, voltage_min_values, label='Min Voltage')
plt.plot(temperature_values, voltage_max_values, label='Max Voltage')

# Highlight the region between minimum and maximum voltages
plt.fill_between(temperature_values, voltage_min_values, voltage_max_values, color='yellow', alpha=0.3)

# Highlight the region between 21°C and 39°C
plt.axvspan(temperature_bandwidth_start, temperature_bandwidth_end, color='cyan', alpha=0.5, label="21°C - 39°C")

plt.xlabel('Temperature (°C)')
plt.ylabel('Voltage across R2 (V)')
plt.title('Voltage across R2 with Changing Temperature')
plt.legend()
plt.grid()
plt.show()
