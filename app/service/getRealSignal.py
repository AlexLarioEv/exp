import matplotlib.pyplot as plt
import pandas as pd

from common import decimateSignal, getTimeSignal, spliningSignal, chartBuilder, mean
from constants import fs, DATA_REAL


def getSignal(path, name):
    try:
        data = pd.read_csv(path, sep='\t', names=[name])
        signal = data[name]
        return signal
    except:
        print('Enter the name file')
        path = f'{DATA_REAL}{input()}.csv'
        return getSignal(path, name)


signal = getSignal(f'{DATA_REAL}DATA.csv', 'pulse_wave')
signal = signal[::-1]
signal, fs = decimateSignal(signal, fs, 100)
time = getTimeSignal(signal, fs)

# chartBuilder(time, signal,title="Исходный сигнал", label="Сигнал пульсовой волны", nameX="Время", nameY="Напряжение")

basic_line_signal, time = spliningSignal(signal, 10, fs)
clean_signal = signal - basic_line_signal

# chartBuilder(time, clean_signal, title="Сигнал с удаленным дрефом изолинии", label="Сигнал пульсовой волны", nameX="Время", nameY="Амплитуда")
amplit_const = mean(signal)
