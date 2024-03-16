import matplotlib.pyplot as plt

from breath import resperator_signal, time_res, peaks_res
from pulse import puls_signal, time as puls_time, peaks_pulse

from common import multipleChartBuilder

fig, axs = plt.subplots(2, 1, figsize=(8, 6))

multipleChartBuilder(axs, puls_time, puls_signal, peaks_pulse, label = 'Пульсовые волны', nameX = 'Время',nameY = 'Амплитуда', count = 0)(axs, time_res, resperator_signal, peaks_res, label = 'Дыхательные волны',nameX = 'Время',nameY = 'Амплитуда', count = 1)

plt.tight_layout()
plt.show()


