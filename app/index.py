from breath import resperator_signal,peaks_res
from pulse import puls_signal, fs as fs_puls

import matplotlib.pyplot as plt

from common import  multipleChartBuilder, getTimeSignal

micr_signal = puls_signal - resperator_signal

micr_time = getTimeSignal(micr_signal, fs_puls)

fig, axs = plt.subplots(2, 1, figsize=(8, 6))

multipleChartBuilder(axs, micr_time, micr_signal, title='Сигнал пульсовой волны', label = 'Пульсовые волны', nameX = 'Время', nameY = 'Амплитуда', count = 0)(axs, getTimeSignal(resperator_signal, fs_puls), resperator_signal, peaks_res, title='Сигнал дыхательной волны', label = 'Дыхательные волны', nameX = 'Время', nameY = 'Амплитуда', count = 1)

plt.tight_layout()
plt.show()
