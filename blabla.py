# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.interpolate import UnivariateSpline

# # Имитационный сигнал
# signal = np.genfromtxt("./DataExp/DATA1.csv", delimiter=',')

# # Определение параметров сплайна
# time = np.arange(len(signal))
# spline_degree = 3
# spline_smoothing_factor = 0.001 * len(signal)

# # Создание сплайна
# spline = UnivariateSpline(time, signal, k=spline_degree, s=spline_smoothing_factor)

# # Определение частоты дыхания
# respiratory_frequency = 12.5

# # Определение интервала времени, соответствующего дыхательным волнам
# respiratory_interval = 1.0 / respiratory_frequency

# # Создание временного ряда для дыхательных волн
# respiratory_time = np.arange(0, time[-1], respiratory_interval)

# # Вычисление значений сплайна в точках временного ряда для дыхательных волн
# respiratory_signal = spline(respiratory_time)

# # Построение графиков
# fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# # График исходного сигнала и сплайна
# axs[0].plot(time, signal, label='Signal')
# axs[0].plot(time, spline(time), label='Spline')
# axs[0].set_xlabel('Time')
# axs[0].set_ylabel('Signal')
# axs[0].legend()

# # График дыхательных волн
# axs[1].plot(respiratory_time, respiratory_signal, label='Respiratory Waves')
# axs[1].set_xlabel('Time')
# axs[1].set_ylabel('Signal')
# axs[1].legend()

# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.interpolate import UnivariateSpline
from scipy.signal import welch

# Генерируем сигнал
fs = 1000  # Частота дискретизации, Гц
t = np.arange(0, 10, 1/fs)  # Время, с
f_pulse = 1  # Частота пульсовой волны, Гц
f_resp = 0.2  # Частота дыхательной волны, Гц
pulse = np.sin(2*np.pi*f_pulse*t)
resp = np.sin(2*np.pi*f_resp*t)
signal = pulse + resp

# Вычисляем спектр сигнала
freqs, psd = welch(signal, fs, nperseg=1024)

# Определяем диапазон частот пульсовой волны
f_pulse_range = (0.8, 1.2)  # Гц
idx_pulse = np.where((freqs >= f_pulse_range[0]) & (freqs <= f_pulse_range[1]))

# Вычисляем аппроксимацию пульсовой волны при помощи сплайнов
spline_pulse = UnivariateSpline(freqs[idx_pulse], psd[idx_pulse], s=0)

# Вычисляем аппроксимацию пульсовой волны для всего диапазона частот
spline_psd = spline_pulse(freqs)

# Вычитаем аппроксимацию пульсовой волны из исходного сигнала
signal_without_pulse = signal - spline_psd

# Строим графики
fig, ax = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
ax[0].plot(t, pulse, 'b-', label='Pulse wave')
ax[0].plot(t, resp, 'g-', label='Respiratory wave')
ax[0].plot(t, signal, 'r-', label='Signal')
ax[0].set_ylabel('Amplitude')
ax[0].legend()
ax[1].plot(freqs, psd, 'b-', label='Signal spectrum')
ax[1].plot(freqs[idx_pulse], psd[idx_pulse], 'r-', label='Pulse wave spectrum')
ax[1].plot(freqs, spline_psd, 'g-', label='Pulse wave approximation')
ax[1].set_ylabel('Amplitude')
ax[1].legend()

plt.show()