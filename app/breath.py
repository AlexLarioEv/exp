import numpy as np
import matplotlib.pyplot as plt

from signalPulse import signal, fs, time
from scipy.signal import find_peaks

from common import chartBuilder, multipleChartBuilder, spliningSignal, fftSignal, filterButter, normalizeSignal, getTimeSignal, splitSignal, cutSignal

# chartBuilder(time, signal,title="Исходный сигнал", label="Сигнал пульсовой волны", nameX="Время", nameY="Напряжение")

basic_line_signal, time = spliningSignal(signal, 10, fs)
spline_signal = signal - basic_line_signal

arr = np.arange(start=0.01, stop=10.01, step=0.01)


# Поиск оптимального коэффициента сглаживания сплайна для выделения дыхательных волн
# TODO: Надо изменить условие выхода из цикла и
# fix me: DATA4 алогритм не работает однако в старом билде все ок. Предварительно из-за децимация. Если увеличить точность (step) все ок.

for i in arr:

    resperator_signal, time = spliningSignal(spline_signal, i, fs) # DATA1 0.9 DATA2 0.3 DATA3 0.95 DATA4 0.28 DATA6 0.19!!!
    
    freg_mag, freq_scale = fftSignal(resperator_signal, time)
    
    peaks, _ = find_peaks(freg_mag[(freq_scale >= 0) & (freq_scale <= 50)])

    if len(peaks)<=1:
        # print(i)
        print('breath',freq_scale[peaks][0])
        # # Вывод пиков на графике
        plt.plot(freq_scale, freg_mag)
        plt.plot(freq_scale[peaks], freg_mag[peaks], "x")
        plt.show()
        break


puls_signal = filterButter(spline_signal, 5, fs)

freg_mag_puls, freq_scale_puls = fftSignal(puls_signal, time)

peaks_puls, _ = find_peaks(freg_mag_puls)

max_peak_puls = peaks_puls[np.argmax(freg_mag_puls[peaks_puls])]

print('puls',freq_scale_puls[max_peak_puls])

chartBuilder(freq_scale_puls, freg_mag_puls, max_peak_puls)


puls_signal  = normalizeSignal(puls_signal)
peaks_pulse , _ = find_peaks(puls_signal, width=110)

resperator_signal, time_res = cutSignal(resperator_signal, fs)
resperator_signal  = normalizeSignal(resperator_signal)
peaks_res , _ = find_peaks(resperator_signal)

fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# fix me: надо предложить какой-то другой вариант построение мулти гравиков
multipleChartBuilder(axs, time, puls_signal, peaks_pulse, label = 'Пульсовые волны', nameX = 'Время',nameY = 'Амплитуда', count = 0)(axs, time_res, resperator_signal, peaks_res, label = 'Дыхательные волны',nameX = 'Время',nameY = 'Амплитуда', count = 1)
plt.tight_layout()
plt.show()