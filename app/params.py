import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import find_peaks
from breath import resperator_signal, time_res, peaks_res
from pulse import puls_signal, time as puls_time, peaks_pulse
from common import getTimeSignal,splitSignal

from common import multipleChartBuilder, chartBuilder

fig, axs = plt.subplots(2, 1, figsize=(8, 6))

multipleChartBuilder(axs, puls_time, puls_signal, peaks_pulse, label = 'Пульсовые волны', nameX = 'Время',nameY = 'Амплитуда', count = 0)(axs, time_res, resperator_signal, peaks_res, label = 'Дыхательные волны',nameX = 'Время',nameY = 'Амплитуда', count = 1)

plt.tight_layout()
plt.show()

# resperator_signal =  np.diff(resperator_signal)

# chartBuilder(getTimeSignal(resperator_signal, 1000),resperator_signal )
min_peaks_res , _ = find_peaks(-resperator_signal)

peaks = [*min_peaks_res,*peaks_res]

signals = splitSignal(resperator_signal, peaks )

print(signals)

chartBuilder(getTimeSignal(signals[3], 1000), signals[3])


