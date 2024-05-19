import pandas as pd
import matplotlib.pyplot as plt

from common import spliningSignal, chartBuilder

filepath_bidmc = './db/open/bidmc_01_Signals.csv'
data_bidmc = pd.read_csv(filepath_bidmc)

# Удаление пробелов из имен столбцов
data_bidmc.columns = data_bidmc.columns.str.strip()

# Функция для выделения 10-секундного интервала
def extract_10s_interval(data, time_column, signal_column, interval_duration, sampling_rate):
    time = data[time_column]
    signal = data[signal_column]
    
    num_points = int(interval_duration * sampling_rate)
    
    interval_time = time[:num_points]
    interval_signal = signal[:num_points]
    
    return interval_time, interval_signal

# Указываем параметры для выделения интервала
interval_duration = 10  # секунды
sampling_rate = 125  # Гц

time_column = 'Time [s]'
pleth_column = 'PLETH'
interval_time, interval_signal = extract_10s_interval(data_bidmc, time_column, pleth_column, interval_duration, sampling_rate)

fs = sampling_rate
signal = interval_signal
time = interval_time

basic_line_signal, time = spliningSignal(signal, 10, fs)

clean_signal = signal - basic_line_signal

# chartBuilder(time, clean_signal)