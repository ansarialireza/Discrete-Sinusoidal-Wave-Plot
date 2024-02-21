import numpy as np
import matplotlib.pyplot as plt

class SinusoidalWavePlotter:
    def __init__(self, sampling_rate=1000000, frequency=1000, duration=5):
        """
        Initialize the SinusoidalWavePlotter.

        Parameters:
        - sampling_rate (int): Number of samples per second.
        - frequency (int): Frequency of the sinusoidal wave in Hertz.
        - duration (int): Duration of the generated waveform in seconds.
        """
        self.sampling_rate = sampling_rate
        self.frequency = frequency
        self.T = 1 / frequency
        self.t = np.arange(0, duration * self.T, 1 / sampling_rate)

    def generate_wave(self):
        """
        Generate a sinusoidal wave.

        Returns:
        - numpy.ndarray: Array containing the values of the generated sinusoidal wave.
        """
        return np.sin(2 * np.pi * self.frequency * self.t)

    def plot_wave(self):
        """
        Plot the generated sinusoidal wave.
        """
        plt.figure(figsize=(10, 4))

        signal = self.generate_wave()

        plt.plot(self.t, signal, label='Sinusoidal Wave', color='#4CAF50', linewidth=2, alpha=0.8)
        plt.title(f'Sinusoidal Wave with a Frequency of {self.frequency} Hz', fontsize=18, fontweight='bold', color='#333333')
        plt.xlabel('Time (seconds)', fontsize=14, fontweight='bold', color='#555555')
        plt.ylabel('Amplitude', fontsize=14, fontweight='bold', color='#555555')
        plt.grid(True, linestyle='--', alpha=0.3)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.minorticks_on()
        plt.grid(which='minor', linestyle='--', alpha=0.1)
        plt.legend(shadow=True)

    def save_plot(self, filename='sinusoidal_wave_plot.png'):
        """
        Save the generated plot as a PNG file.

        Parameters:
        - filename (str): Name of the file to save.
        """
        plt.savefig(filename, dpi=300, bbox_inches='tight', transparent=False, facecolor='white')

    def show_plot(self):
        """
        Display the generated plot.
        """
        plt.show()

# Usage
plotter = SinusoidalWavePlotter(sampling_rate=1000000, frequency=1000, duration=5)
plotter.plot_wave()
plotter.save_plot()
plotter.show_plot()
