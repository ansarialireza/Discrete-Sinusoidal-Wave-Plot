import numpy as np
import matplotlib.pyplot as plt

# Define parameters
fs = 1000000  # Increased sampling rate (number of samples per second)
f = 1000  # Signal frequency (Hz)
T = 1 / f  # Signal period (seconds)
t = np.arange(0, 5 * T, 1/fs)  # Discrete time (from 0 to 5 periods)

# Generate a sinusoidal wave
signal = np.sin(2 * np.pi * f * t)

# Plot the waveform with improved styling
plt.figure(figsize=(10, 4))  # Set figure size

# Plot the sinusoidal wave with a smooth gradient color
plt.plot(t, signal, label='Sinusoidal Wave', color='#4CAF50', linewidth=2, alpha=0.8)

# Enhance title and axis labels with a modern font
plt.title('Sinusoidal Wave with a Frequency of 1000 Hz', fontsize=18, fontweight='bold', color='#333333')
plt.xlabel('Time (seconds)', fontsize=14, fontweight='bold', color='#555555')
plt.ylabel('Amplitude', fontsize=14, fontweight='bold', color='#555555')

# Lighten the grid lines and add a subtle background color
plt.grid(True, linestyle='--', alpha=0.3)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.minorticks_on()
plt.grid(which='minor', linestyle='--', alpha=0.1)

# Add a shadow to the legend for better visibility
plt.legend(shadow=True)

# Save the figure as a PNG file with higher resolution and a transparent background
plt.savefig('sinusoidal_wave_plot.png', dpi=300, bbox_inches='tight', transparent=True)

# Display the plot
plt.show()
