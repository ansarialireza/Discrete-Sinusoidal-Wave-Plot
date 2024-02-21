import numpy as np
import matplotlib.pyplot as plt

# Define parameters
fs = 100000  # Increased sampling rate (number of samples per second)
f = 1000  # Signal frequency (Hz)
T = 1 / f  # Signal period (seconds)
t = np.arange(0, 5 * T, 1/fs)  # Discrete time (from 0 to 5 periods)

# Generate a sinusoidal wave
signal = np.sin(2 * np.pi * f * t)

# Plot the waveform with improved styling
plt.figure(figsize=(10, 4))  # Set figure size
plt.plot(t, signal, label='Sinusoidal Wave', color='green', linewidth=2)
plt.title('Sinusoidal Wave with a Frequency of 1000 Hz', fontsize=16)
plt.xlabel('Time (seconds)', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
