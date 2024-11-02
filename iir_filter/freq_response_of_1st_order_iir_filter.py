import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Coefficients of the transfer function H(z) = (b0 + b1*z^-1) / (1 + a1*z^-1)
b = [0.1, -0.0]  # Numerator coefficients
a = [1, -0.9]  # Denominator coefficients

# Sampling rate in Hz
fs = 60  # Sampling frequency in Hz

# Compute the frequency response using scipy.signal.freqz
w, h = signal.freqz(b, a, worN=8000)

# Convert from radians/sample to Hz
frequencies_hz = w * fs / (2 * np.pi)

# Plot magnitude response
plt.figure(figsize=(10, 6))

# Plot magnitude
plt.subplot(2, 1, 1)
plt.plot(frequencies_hz, 20 * np.log10(abs(h)), 'b')
plt.title('Frequency Response')
plt.ylabel('Magnitude [dB]')
plt.xlabel('Frequency [Hz]')
plt.grid()

# Plot phase response
plt.subplot(2, 1, 2)
plt.plot(frequencies_hz, np.angle(h), 'r')
plt.ylabel('Phase [radians]')
plt.xlabel('Frequency [Hz]')
plt.grid()

# Show plot
plt.tight_layout()
plt.show()
