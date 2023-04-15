import pandas as pd
import numpy as np
import pywt
from scipy import signal
from scipy.signal import find_peaks
from scipy.fft import  fft, fftfreq
from matplotlib import pyplot as plt
from matplotlib import style
from dateutil import parser as dt_parser
 
headers = ['signal']
data = pd.read_csv("./DataExp/DATA2_2023-04-11_0_153133.Wfm.csv", sep='\t', names=headers)
data= data.assign(time= data.index + 1)

timeData= data["time"]
signalData = data["signal"]
fs= 100000
time = np.linspace(0, 10, fs*10)


def fftSignal(signalData, time ):
    freq_domain = np.fft.fft(signalData)

    freq_mag = np.abs(freq_domain)
    freq_mag = freq_mag[:len(freq_mag) // 2]
    freq_scale = np.fft.fftfreq(len(signalData), d=time[1]-time[0])
    freq_scale = freq_scale[:len(freq_scale) // 2]

    fig, ax = plt.subplots()
    ax.plot(freq_scale[3:100], freq_mag[3:100])
    ax.set_ylabel('Amplitude')
    plt.show()
    return freq_mag 


def filterButterSignal(signalData, time, cutoff_freq, fs, order=4):
    nyq_freq = 0.5*fs 
    b, a = signal.butter(order, cutoff_freq/nyq_freq, btype='low')
    filterSignal = signal.filtfilt(b, a, signalData)

    plt.plot(time, filterSignal , markersize=3)
    plt.show()
    return filterSignal

freq_mag=fftSignal(signalData, time)

filterSignalPusle = filterButterSignal(signalData, time, 0.4, fs, 4)

freq_mag=fftSignal(filterSignalPusle, time)

# filterSignalWaves = filterButterSignal(filterSignalPusle, time, 0.4, fs)


peaks, _ = find_peaks(freq_mag[3:8])

print(peaks)
