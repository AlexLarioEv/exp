import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Generate a signal
fs = 1000
t = np.arange(0, 10, 1/fs)
f_pulse = 1
f_resp = 0.2
pulse = np.sin(2*np.pi*f_pulse*t)
resp = np.sin(2*np.pi*f_resp*t)
signal = pulse + resp

# Calculate the PSD of the signal
f, psd = signal.welch(signal, fs, nperseg=1024)

# Plot the results
plt.semilogy(f, psd)
plt.xlabel('Frequency (Hz)')
plt.ylabel('PSD (V^2 / Hz)')
plt.show()