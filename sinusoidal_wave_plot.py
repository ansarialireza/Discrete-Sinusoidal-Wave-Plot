import numpy as np
import matplotlib.pyplot as plt

class DiscreteSinusoidalWavePlotter:
    def __init__(self, sampling_rate=1000, frequency=10, duration=5):
        """
        Initialize the DiscreteSinusoidalWavePlotter.

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
        Generate a discrete sinusoidal wave.

        Returns:
        - numpy.ndarray: Array containing the values of the generated discrete sinusoidal wave.
        """
        return np.sin(2 * np.pi * self.frequency * self.t)

    def plot_wave(self):
        """
        Plot the generated discrete sinusoidal wave.
        """
        plt.figure(figsize=(10, 4))

        signal = self.generate_wave()

        plt.stem(self.t, signal, basefmt="b", label='Discrete Sinusoidal Wave')
        plt.title(f'Discrete Sinusoidal Wave with a Frequency of {self.frequency} Hz', fontsize=18, fontweight='bold', color='#333333')
        plt.xlabel('Time (seconds)', fontsize=14, fontweight='bold', color='#555555')
        plt.ylabel('Amplitude', fontsize=14, fontweight='bold', color='#555555')
        plt.grid(True, linestyle='--', alpha=0.3)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.minorticks_on()
        plt.grid(which='minor', linestyle='--', alpha=0.1)
        plt.legend(shadow=True)

    def save_plot(self, filename='discrete_sinusoidal_wave_plot.png'):
        """
        Save the generated plot of the discrete sinusoidal wave as a PNG file.

        Parameters:
        - filename (str): Name of the file to save.
        """
        plt.savefig(filename, dpi=300, bbox_inches='tight', transparent=False, facecolor='white')

    def show_plot(self):
        """
        Display the generated plot of the discrete sinusoidal wave.
        """
        plt.show()

# Usage
plotter = DiscreteSinusoidalWavePlotter(sampling_rate=27000, frequency=1000, duration=5)
plotter.plot_wave()
plotter.save_plot()
plotter.show_plot()
