import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import find_peaks

from getSignal import *
from transformSIgnals import *
from chartBuilder import *
from constants import fs

# TODO: нет DATA9

signal = getSignal("./db/DATA3.csv", 'pulse_wave')
signal, fs = decimateSignal(signal, fs, 100)
time = getTimeSignal(signal, fs)

chartBuilder(time, signal,title="Исходный сигнал", label="Сигнал пульсовой волны", nameX="Время", nameY="Напряжение")

# Создание сплайна

basic_line_signal, time = spliningSignal(signal, 10, fs)
spline_signal = signal - basic_line_signal

arr = np.arange(start=0.01, stop=10.01, step=0.01)


# Поиск оптимального коэффициента сглаживания сплайна для выделения дыхательных волн
# TODO: Надо изменить условие выхода из цикла и
# fix me: DATA4 алогритм не работает однако в старом билде все ок. Предварительно из-за децимация

for i in arr:

    resperator_signal, time = spliningSignal(spline_signal, i, fs) # DATA1 0.9 DATA2 0.3 DATA3 0.95 DATA4 0.28 DATA6 0.19!!!
    
    freg_mag, freq_scale = fftSignal(resperator_signal, time)
    
    peaks, _ = find_peaks(freg_mag[(freq_scale >= 0) & (freq_scale <= 50)])

    if len(peaks)<=1:
        print(i)
        # print(peaks)
        # # Вывод пиков на графике
        plt.plot(freq_scale, freg_mag)
        plt.plot(freq_scale[peaks], freg_mag[peaks], "x")
        plt.show()
        break


filter_signal = filterButter(spline_signal, 5, fs)
filter_signal  = normalizeSignal(filter_signal)
peaks_pulse , _ = find_peaks(filter_signal)

peaks_pulse_min , _ = find_peaks(-filter_signal,width=110)

signals = splitSignal(filter_signal,peaks_pulse_min)

chartBuilder(time, filter_signal,peaks_pulse_min, "Сигнал после устранения помехов", "Сигнал пульсовой волны", "Время", "Напряжение")

fig, axs = plt.subplots(2, 1, figsize=(8, 6))

multipleChartBuilder( axs ,getTimeSignal(signals[11],fs),signals[11], count = 0)( axs ,getTimeSignal(signals[12],fs),signals[12], count = 1)
plt.tight_layout()
plt.show()


resperator_signal, time_res = cutSignal(resperator_signal, fs)
resperator_signal  = normalizeSignal(resperator_signal)

peaks_res , _ = find_peaks(resperator_signal)

# Построение графиков
fig, axs = plt.subplots(2, 1, figsize=(8, 6))


# fix me: надо предложить какой-то другой вариант построение мулти гравиков
multipleChartBuilder(axs, time, filter_signal, label = 'Пульсовые волны', nameX = 'Время',nameY = 'Амплитуда', count = 0)(axs, time_res, resperator_signal, peaks_res, label = 'Дыхательные волны',nameX = 'Время',nameY = 'Амплитуда', count = 1)
plt.tight_layout()
plt.show()
