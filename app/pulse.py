import numpy as np
import matplotlib.pyplot as plt

from cleanSignal import clean_signal, fs, time
from scipy.signal import find_peaks

from common import chartBuilder, multipleChartBuilder, fftSignal, filterButter, normalizeSignal, getTimeSignal, splitSignal, cutSignal

puls_signal = filterButter(clean_signal, 5, fs)

# freg_mag_puls, freq_scale_puls = fftSignal(puls_signal, time)
# peaks_puls, _ = find_peaks(freg_mag_puls)
# max_peak_puls = peaks_puls[np.argmax(freg_mag_puls[peaks_puls])]
# chartBuilder(freq_scale_puls, freg_mag_puls, max_peak_puls)

puls_signal  = normalizeSignal(puls_signal)
peaks_pulse , _ = find_peaks(puls_signal, width=110)

# chartBuilder( time, puls_signal, peaks_pulse, label = 'Пульсовые волны', nameX = 'Время',nameY = 'Амплитуда')