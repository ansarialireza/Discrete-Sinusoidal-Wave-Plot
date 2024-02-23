import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

class FourierSeriesPlotter:
    def __init__(self, interpolation_points, interval_start, interval_end, num_terms):
        self.interpolation_points = interpolation_points
        self.interval_start = interval_start
        self.interval_end = interval_end
        self.num_terms = num_terms
        self.T = interval_end - interval_start
        self.a_coefficients = self.calculate_a_coefficients()

    def original_function(self, x):
        return np.interp(x, self.interpolation_points[0], self.interpolation_points[1])

    def calculate_a_coefficients(self):
        calculate_an = lambda n: (2 / self.T) * quad(
            lambda x: self.original_function(x) * np.cos(2 * np.pi * n / self.T * x),
            -self.T / 2, self.T / 2
        )[0]

        return [calculate_an(n) for n in range(self.num_terms)]

    def even_function(self, x):
        return self.a_coefficients[0] / 2 + sum(
            a * np.cos(2 * np.pi * n / self.T * x) for n, a in enumerate(self.a_coefficients[1:], start=1)
        )

    def odd_function(self, x):
        return sum(0 * np.sin(2 * np.pi * n / self.T * x) for n in range(1, self.num_terms))

    def plot_functions(self, save_path=None):
        x_values = np.arange(self.interval_start, self.interval_end, 0.01)
        y_even = self.even_function(x_values)
        y_odd = self.odd_function(x_values)

        plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_even, label='f_even(x)', linestyle='--', linewidth=2, color='orange')
        plt.plot(x_values, y_odd, label='f_odd(x)', linestyle='--', linewidth=2, color='green')
        plt.title('Plot of Even and Odd Functions')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.scatter(self.interpolation_points[0], self.interpolation_points[1], color='red', label='Data Points')
        plt.legend()

        if save_path:
            plt.savefig(save_path)
            plt.close()
        else:
            plt.show()

# Example usage:
interpolation_points = ([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6], [0, 0, 0, 1, 1, 1, 1, 1, 0, 0])
interval_start = -3
interval_end = 6
num_terms = 10

plotter = FourierSeriesPlotter(interpolation_points, interval_start, interval_end, num_terms)
plotter.plot_functions(save_path="even_odd_functions.png")
