import numpy as np

from service.getRealSignal import clean_signal, fs, time
from scipy.signal import find_peaks

from common import chartBuilder, multipleChartBuilder, spliningSignal, fftSignal, normalizeSignal, getTimeSignal

arr = np.arange(start=0.01, stop=10.01, step=0.005)

for i in arr:

    resperator_signal, time = spliningSignal(clean_signal, i, fs) # DATA1 0.9 DATA2 0.3 DATA3 0.95 DATA4 0.28 DATA6 0.19!!!
    
    freg_mag, freq_scale = fftSignal(resperator_signal, time)
    
    peaks, _ = find_peaks(freg_mag[(freq_scale >= 0) & (freq_scale <= 50)])

    if len(peaks)<=1:
        # print(i)
        # print('breath',freq_scale[peaks][0])
        # # Вывод пиков на графике
        # chartBuilder(freq_scale, freg_mag, peaks)
        break

resperator_signal  = normalizeSignal(resperator_signal)
time_res = getTimeSignal(resperator_signal, fs)

max_peaks_res , _ = find_peaks(resperator_signal)
min_peaks_res , _ = find_peaks(-resperator_signal)

peaks_res = sorted([*min_peaks_res, *max_peaks_res])

chartBuilder(time_res, resperator_signal, peaks_res, label = 'Дыхательные волны', nameX = 'Время', nameY = 'Амплитуда')
