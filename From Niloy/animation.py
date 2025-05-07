import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the time domain
t = np.linspace(0, 2*np.pi, 400)

# Number of Fourier series terms
num_terms = 10  # Change this to see more sine waves being added

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
ax.set_title("Fourier Series Approximation of a Square Wave")
ax.grid()

# Initialize lines
square_wave, = ax.plot(t, np.sign(np.sin(t)), 'k', label="Target Square Wave")
approx_wave, = ax.plot([], [], 'r', label="Fourier Approximation")
sine_waves = [ax.plot([], [], '--', alpha=0.5)[0] for _ in range(num_terms)]

ax.legend()

def fourier_series(t, n):
    """Compute the Fourier series approximation of a square wave."""
    return sum((4 / (np.pi * (2*k-1))) * np.sin((2*k-1) * t) for k in range(1, n+1))

def init():
    approx_wave.set_data([], [])
    for sine in sine_waves:
        sine.set_data([], [])
    return [approx_wave] + sine_waves

def update(frame):
    """Update the animation frame-by-frame."""
    n = frame + 1
    y_approx = fourier_series(t, n)
    approx_wave.set_data(t, y_approx)
    
    # Update individual sine waves
    for k in range(n):
        y_sine = (4 / (np.pi * (2*k+1))) * np.sin((2*k+1) * t)
        sine_waves[k].set_data(t, y_sine)
    
    return [approx_wave] + sine_waves

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_terms, init_func=init, blit=True, repeat=False, interval=500)

plt.show()