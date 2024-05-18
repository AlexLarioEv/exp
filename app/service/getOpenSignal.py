import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Загрузка данных из CSV файла
filepath_bidmc = './db/open/bidmc_01_Signals.csv'
data_bidmc = pd.read_csv(filepath_bidmc)

# Удаление пробелов из имен столбцов
data_bidmc.columns = data_bidmc.columns.str.strip()

# Функция для выделения 10-секундного интервала
def extract_10s_interval(data, time_column, signal_column, interval_duration, sampling_rate):
    time = data[time_column]
    signal = data[signal_column]
    
    # Вычисление количества точек для 10 секундного интервала
    num_points = int(interval_duration * sampling_rate)
    
    # Выделение 10 секундного интервала
    interval_time = time[:num_points]
    interval_signal = signal[:num_points]
    
    return interval_time, interval_signal

# Указываем параметры для выделения интервала
interval_duration = 10  # секунды
sampling_rate = 125  # Гц

# Извлечение 10 секундного интервала сигнала PLETH
time_column = 'Time [s]'
pleth_column = 'PLETH'
interval_time, interval_signal = extract_10s_interval(data_bidmc, time_column, pleth_column, interval_duration, sampling_rate)

print(len(interval_signal))

# Построение графика для 10 секундного интервала
plt.figure(figsize=(14, 7))
plt.plot(interval_time, interval_signal, label=f'{pleth_column} (10 секунд)')
plt.xlabel('Время (секунды)')
plt.ylabel('Амплитуда')
plt.title(f'График 10 секундного интервала сигнала {pleth_column}')
plt.legend()
plt.grid(True)
plt.show()

fs = sampling_rate
signal = interval_signal
time = interval_time
clean_signal = interval_signal