import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, decimate
from scipy.interpolate import UnivariateSpline

def filterButterSignal(signalData, time, cutoff_freq, fs, order=4):
    nyq_freq = 0.5*fs 
    b, a = butter(order, cutoff_freq/nyq_freq, btype='low')
    filterSignal = filtfilt(b, a, signalData)

    plt.plot(time, filterSignal , markersize=3)
    plt.show()
    return filterSignal

def fftSignal(signalData, time ):
    freq_domain = np.fft.fft(signalData)

    freq_mag = np.abs(freq_domain)
    freq_mag = freq_mag[:len(freq_mag) // 2]
    freq_scale = np.fft.fftfreq(len(signalData), d=time[1]-time[0])
    freq_scale = freq_scale[:len(freq_scale) // 2]

    fig, ax = plt.subplots()
    ax.plot(freq_scale[1:100], freq_mag[1:100])
    ax.set_ylabel('Amplitude')
    plt.show()
    return freq_mag 

def splineSignal(signal, time, k, splineDegree = 3): 
    spline_smoothing_factor = 0.001 * len(signal)*10
    return spline = UnivariateSpline(time, signal, k=spline_degree, s=spline_smoothing_factor)

headers = ['signal']
# Имитационный сигнал
data = pd.read_csv("./DataExp/DATA7.csv", sep='\t', names=headers)
signal = data["signal"]

signal = decimate(signal, 10)
signal = decimate(signal, 10)

# Определение параметров сплайна
time = np.arange(len(signal))
spline_degree = 3
spline_smoothing_factor = 0.001 * len(signal)*10  # DATA2 = len(signal)/2.5  DATA3 = 1.12 c удалением по 500   DATA4 = 0.42 DATA5 = 0.5  DATA6 = 
spline_smoothing_factor2 = 0.001 * len(signal)/10
spline_smoothing_factor3 = 0.001 * len(signal)/19 # DATA6 = 2.95
# Создание сплайна


filterButterSignal(signal, time, 10, 100000/100)

spline = UnivariateSpline(time, signal, k=spline_degree, s=spline_smoothing_factor)

spline2 = UnivariateSpline(time, signal, k=spline_degree, s=spline_smoothing_factor2)

# Определение частоты дыхания
respiratory_frequency = 12.5

# Определение интервала времени, соответствующего дыхательным волнам
respiratory_interval = 1.0 / respiratory_frequency

# Создание временного ряда для дыхательных волн
respiratory_time = np.arange(0, time[-1], respiratory_interval)

# Вычисление значений сплайна в точках временного ряда для дыхательных волн
respiratory_signal = spline(respiratory_time)
puls = spline2(respiratory_time)
respiratory_signal = puls - respiratory_signal

spline = UnivariateSpline(time, signal, k=spline_degree, s=spline_smoothing_factor3)

respiratory_signal = spline(respiratory_time)


fftSignal(respiratory_signal, time)

# Построение графиков
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# График исходного сигнала и сплайна
axs[0].plot(time, signal, label='Signal')
axs[0].plot(time, spline(time), label='Spline')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Signal')
axs[0].legend()

# График дыхательных волн
axs[1].plot(respiratory_time, respiratory_signal, label='Respiratory Waves')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Signal')
axs[1].legend()

plt.show()