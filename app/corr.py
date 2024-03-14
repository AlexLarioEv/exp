import matplotlib.pyplot as plt

from scipy.signal import find_peaks

from signalPulse import signal, fs
from common import  getTimeSignal, spliningSignal, filterButter, normalizeSignal,splitSignal, chartBuilder, multipleChartBuilder

basic_line_signal, time = spliningSignal(signal, 10, fs)
spline_signal = signal - basic_line_signal

filter_signal = filterButter(spline_signal, 5, fs)
filter_signal_norm  = normalizeSignal(filter_signal)

peaks_pulse_min , _ = find_peaks(-filter_signal_norm, width=110)

chartBuilder(time, filter_signal_norm, peaks_pulse_min, "Сигнал после устранения помехов", "Сигнал пульсовой волны", "Время", "Напряжение")

signals = splitSignal(filter_signal_norm,peaks_pulse_min)

fig, axs = plt.subplots(2, 1, figsize=(8, 6))

multipleChartBuilder( axs ,getTimeSignal(signals[11],fs),signals[11], count = 0)( axs ,getTimeSignal(signals[12],fs),signals[12], count = 1)

plt.tight_layout()
plt.show()
