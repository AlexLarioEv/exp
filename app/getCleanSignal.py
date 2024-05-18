from service import getSignal
from common import decimateSignal, getTimeSignal, spliningSignal, chartBuilder, mean,filterButter

from constants import fs

# TODO: нет DATA9

signal = getSignal('./db/DATA10.csv', 'pulse_wave')
signal = signal[::-1]

# Понижение дискретизации двумя функциями. Для повышения точности 
signal, fs = decimateSignal(signal, fs, 10)
signal, fs = decimateSignal(signal, fs, 10)

time = getTimeSignal(signal, fs)

# chartBuilder(time, signal,title="Исходный сигнал", label="Сигнал пульсовой волны", nameX="Время", nameY="Напряжение")
 
amplit_const = mean(signal)

basic_line_signal, time = spliningSignal(signal, 10, fs)
clean_signal = signal - basic_line_signal

# chartBuilder(time, basic_line_signal,title="Дрейф изолинии", nameX="Время", nameY="Амплитуда")

chartBuilder(time, clean_signal,title="Исходный сигнал без дрейфа изолинии", label="Сигнал пульсовой волны", nameX="Время", nameY="Амплитуда")