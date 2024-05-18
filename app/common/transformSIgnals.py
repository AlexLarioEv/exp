import numpy as np

from scipy.signal import butter, filtfilt,decimate,freqz
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt

from constants import FREQUENCY_WINDOW

def decimateSignal(signal, fs, k):
    signal = decimate(signal, k)   
    fs = fs/k
    return signal, fs

def filterButter(signal_data, cutoff_freq, fs, order=4):
    nyq_freq = 0.5 * fs
    b, a = butter(order, cutoff_freq/nyq_freq, btype='low')
    w, h = freqz(b, a, worN=8000)
    freq = w * fs / (2 * np.pi)
    plt.semilogx(freq, 20*np.log10(abs(h)))
    plt.title('Амплитудная характеристика фильтра Баттерворта')
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Амплитуда (дБ)')
    plt.margins(0, 0.1)
    plt.grid(which='both', axis='both')
    plt.show()
    filter_signal = filtfilt(b, a, signal_data)

    return filter_signal

def fftSignal(signal_data, time ):
    freq_domain = np.fft.fft(signal_data)
    freq_mag = np.abs(freq_domain)
    freq_mag = freq_mag[:len(freq_mag) // 2]
    freq_scale = np.fft.fftfreq(len(signal_data), d=time[1]-time[0])
    freq_scale = freq_scale[:len(freq_scale) // 2]

    return freq_mag[0:FREQUENCY_WINDOW],freq_scale[0:FREQUENCY_WINDOW]

def spliningSignal(signal, s, fs, spline_degree = 3):
    time = np.arange(len(signal))/fs
    spline_smoothing_factor = 0.001 * len(signal)*s
    spline = UnivariateSpline(time, signal, k = spline_degree, s = spline_smoothing_factor)
    splineSignal = spline(time)
    return splineSignal, time

def cutSignal(signal, fs):
    # находим индексы смены знака
    zero_crossings = np.where(np.diff(np.sign(signal)))[0]

    # отрезаем начало и конец до первого и последнего знака
    trimmed_signal = signal[zero_crossings[0]+1:zero_crossings[-1]+1]

    time = np.arange(len(trimmed_signal)) / fs

    return trimmed_signal, time

def cutSignal(signal, fs):
    # находим индексы смены знака
    zero_crossings = np.where(np.diff(np.sign(signal)))[0]

    # отрезаем начало и конец до первого и последнего знака
    trimmed_signal = signal[zero_crossings[0] + 1:zero_crossings[-1] + 1]

    time = np.arange(len(trimmed_signal))/fs

    return trimmed_signal, time

getTimeSignal = lambda signal, fs: np.arange(len(signal))/fs 

def normalizeSignal(signal): 
    max_peak = max(signal)
    min_peak = -min(signal)

    if(max_peak>min_peak):
        return signal / max_peak
    
    return signal / min_peak

def splitSignal(signal, separators):
    counter = 0
    start_separator = 0
    signals={}

    for i in separators:
        end_separator = i
        part_of_signal = signal[start_separator:end_separator]
        start_separator = end_separator
        signals[counter] = part_of_signal
        counter = counter + 1

    return signals

# Среднее значение числового ряда
def mean(xs): 
    return sum(xs) / len(xs) 

def compoundPeaks(min, max): 
    return sorted([*min, *max])