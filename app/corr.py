from scipy.signal import find_peaks

from getSignal import getSignal
from transformSIgnals import decimateSignal, getTimeSignal, spliningSignal, filterButter, normalizeSignal,splitSignal
from chartBuilder import *
from constants import fs


signal = getSignal("./db/DATA3.csv", 'pulse_wave')
signal, fs = decimateSignal(signal, fs, 100)
time = getTimeSignal(signal, fs)

basic_line_signal, time = spliningSignal(signal, 10, fs)
spline_signal = signal - basic_line_signal

filter_signal = filterButter(spline_signal, 5, fs)
filter_signal  = normalizeSignal(filter_signal)
peaks_pulse , _ = find_peaks(filter_signal)

peaks_pulse_min , _ = find_peaks(-filter_signal,width=110)

signals = splitSignal(filter_signal,peaks_pulse_min)
# print(getTimeSignal(signals, fs), signals)
chartBuilder(getTimeSignal(signals[2], fs), signals[2])

obj = {}

print( ''.__reduce_ex__.__dir__)