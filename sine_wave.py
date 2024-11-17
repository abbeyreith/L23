import numpy as np
import matplotlib.pyplot as plt

def plot_sine_wave(frequency=1):
    x = np.linspace(0, 2 * np.pi, 1000)  # Generate 1000 points between 0 and 2π
    y = np.sin(frequency * x)            # Calculate sine wave
    plt.plot(x, y)
    plt.title(f'Sine Wave with Frequency {frequency} Hz')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.grid()
    plt.show()

# Call the function to plot
plot_sine_wave()
