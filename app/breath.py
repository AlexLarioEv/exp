import numpy as np

from getCleanSignal import clean_signal, fs, time
from scipy.signal import find_peaks

from common import chartBuilder, multipleChartBuilder, spliningSignal, fftSignal, filterButter, normalizeSignal, getTimeSignal, splitSignal, cutSignal

# Поиск оптимального коэффициента сглаживания сплайна для выделения дыхательных волн
# TODO: Надо изменить условие выхода из цикла и
# fix me: DATA4 алогритм не работает однако в старом билде все ок. Предварительно из-за децимация. Если увеличить точность (step) все ок.
arr = np.arange(start=0.01, stop=10.01, step=0.005)

for i in arr:

    resperator_signal, time = spliningSignal(clean_signal, i, fs) # DATA1 0.9 DATA2 0.3 DATA3 0.95 DATA4 0.28 DATA6 0.19!!!
    
    freg_mag, freq_scale = fftSignal(resperator_signal, time)
    
    peaks, _ = find_peaks(freg_mag[(freq_scale >= 0) & (freq_scale <= 5)])

    if len(peaks)<=1:
        # print(i)
        # print('breath',freq_scale[peaks][0])
        # # Вывод пиков на графике
        # chartBuilder(freq_scale, freg_mag, peaks)
        break


resperator_signal, time_res = cutSignal(resperator_signal, fs)
resperator_signal  = normalizeSignal(resperator_signal)
peaks_res , _ = find_peaks(resperator_signal)

chartBuilder(time_res, resperator_signal, peaks_res, label = 'Дыхательные волны', nameX = 'Время', nameY = 'Амплитуда')
