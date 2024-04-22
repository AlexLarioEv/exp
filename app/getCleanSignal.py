from service import getSignal
from common import decimateSignal, getTimeSignal, spliningSignal, chartBuilder, mean,filterButter

from constants import fs

# TODO: нет DATA9

signal = getSignal('./db/DATA10.csv', 'pulse_wave')
signal, fs = decimateSignal(signal, fs, 100)
time = getTimeSignal(signal, fs)

# chartBuilder(time, signal,title="Исходный сигнал", label="Сигнал пульсовой волны", nameX="Время", nameY="Напряжение")
 
amplit_const = mean(signal)

basic_line_signal, time = spliningSignal(signal, 10, fs)
clean_signal = signal - basic_line_signal
