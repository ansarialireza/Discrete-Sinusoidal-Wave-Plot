import numpy as np
import matplotlib.pyplot as plt

class SinusoidalWavePlotter:
    def __init__(self, fs=1000000, f=1000, duration=5):
        self.fs = fs
        self.f = f
        self.T = 1 / f
        self.t = np.arange(0, duration * self.T, 1 / fs)

    def generate_wave(self):
        return np.sin(2 * np.pi * self.f * self.t)

    def plot_wave(self):
        plt.figure(figsize=(10, 4))

        signal = self.generate_wave()

        plt.plot(self.t, signal, label='Sinusoidal Wave', color='#4CAF50', linewidth=2, alpha=0.8)
        plt.title(f'Sinusoidal Wave with a Frequency of {self.f} Hz', fontsize=18, fontweight='bold', color='#333333')
        plt.xlabel('Time (seconds)', fontsize=14, fontweight='bold', color='#555555')
        plt.ylabel('Amplitude', fontsize=14, fontweight='bold', color='#555555')
        plt.grid(True, linestyle='--', alpha=0.3)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.minorticks_on()
        plt.grid(which='minor', linestyle='--', alpha=0.1)
        plt.legend(shadow=True)

    def save_plot(self, filename='sinusoidal_wave_plot.png'):
        plt.savefig(filename, dpi=300, bbox_inches='tight', transparent=False, facecolor='white')


    def show_plot(self):
        plt.show()

# Usage
plotter = SinusoidalWavePlotter(fs=1000000, f=1000, duration=5)
plotter.plot_wave()
plotter.save_plot()
plotter.show_plot()
