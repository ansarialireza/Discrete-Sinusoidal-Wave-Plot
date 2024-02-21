# Sinusoidal Wave Plot 🌊

Dive into the mesmerizing world of sinusoidal waves with this Python script that generates and plots a stunning waveform of your chosen frequency.

## Prerequisites

Ensure you have Python and Matplotlib installed on your machine.

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ansarialireza/sinusoidal-wave-plot.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd sinusoidal-wave-plot
   ```

3. **Run the Python script:**
   ```bash
   python sinusoidal_wave_plot.py
   ```
   Watch the magic unfold as the script generates and displays the captivating sinusoidal wave plot.

4. **Optional - Admire the Art:**
   Discover the saved plot as a PNG file in the same directory. Behold the beauty:

   ![Sinusoidal Wave Plot](sinusoidal_wave_plot.png)

   For a closer look, gaze upon the plot directly in GitHub by clicking on the 📈 [Plot Image](sinusoidal_wave_plot.png) link.

## Customization

Feel the power to customize the frequency of the sinusoidal wave by simply modifying the `f` variable in the script.

## Additional Plotting Elegance

For those seeking unparalleled elegance, use a custom plotting class:

   ```python
   plotter = DiscreteSinusoidalWavePlotter(sampling_rate=27000, frequency=1000, duration=5)
   plotter.plot_wave()
   plotter.save_plot()
   plotter.show_plot()
   ```

## Dependencies

- Python
- Matplotlib

## Author

Alireza Ansari 🎨

## License

This project is licensed under the MIT License - see the 📜 [LICENSE](LICENSE) file for details.