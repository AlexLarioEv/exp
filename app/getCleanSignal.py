import matplotlib.pyplot as plt

from service import getSignal
from common import decimateSignal, getTimeSignal, spliningSignal, chartBuilder, multipleChartBuilder

from constants import fs

# TODO: нет DATA9

signal = getSignal('./db/DATA1.csv', 'pulse_wave')
signal, fs = decimateSignal(signal, fs, 100)
time = getTimeSignal(signal, fs)

time_old = time
signal_old=signal

# chartBuilder(time, signal,title="Исходный сигнал", label="Сигнал пульсовой волны", nameX="Время", nameY="Напряжение")

basic_line_signal, time = spliningSignal(signal, 10, fs)
clean_signal = signal - basic_line_signal

# chartBuilder(time, clean_signal, title="Сигнал с удаленным дрефом изолинии", label="Сигнал пульсовой волны", nameX="Время", nameY="Амплитуда")

fig, axs = plt.subplots(2, 1, figsize=(8, 6))

multipleChartBuilder(axs, time_old, signal_old, title='Исходный сигнал', label = 'Сигнал пульсовой волны', nameX = 'Время', nameY = 'Напряжение', count = 0)(axs, time, clean_signal, title='Сигнал с удаленным дрефом изолинии', label = 'Сигнал пульсовой волны', nameX = 'Время', nameY = 'Амплитуда', count = 1)

plt.tight_layout()
plt.show()
