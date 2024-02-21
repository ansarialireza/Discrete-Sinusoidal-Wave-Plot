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
plt.plot(t, signal, label='Sinusoidal Wave', color='#2C7BB6', linewidth=2)  # Use a pleasant color
plt.title('Sinusoidal Wave with a Frequency of 1000 Hz', fontsize=16, color='#333333')  # Darker title color
plt.xlabel('Time (seconds)', fontsize=12, color='#555555')  # Darker x-axis label color
plt.ylabel('Amplitude', fontsize=12, color='#555555')  # Darker y-axis label color
plt.grid(True, linestyle='--', alpha=0.5)  # Lighter grid lines
plt.legend()

# Save the figure as a PNG file with higher resolution
plt.savefig('sinusoidal_wave_plot.png', dpi=300, bbox_inches='tight', transparent=True)

# Show the plot with an interactive grid
plt.grid(True, linestyle='--', alpha=0.5)
plt.minorticks_on()
plt.grid(which='minor', linestyle='--', alpha=0.3)
plt.show()
