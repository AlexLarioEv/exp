from getCleanSignal import clean_signal, time, fs, amplit_const 

from common import getTimeSignal, splitSignal, multipleChartBuilder, chartBuilder, filterButter,compoundPeaks
from scipy.signal import find_peaks

def findMaxAmplitude(amplitude_arr):
    currentAmplitude = 0
    min = 0

    for point in amplitude_arr:
        if(point < 0):
            min = point

        amplitude = point - min

        if(amplitude > currentAmplitude):
            currentAmplitude = amplitude

    return currentAmplitude


ppg = filterButter(clean_signal, 5, fs)

peaks_ppg_max , _ = find_peaks(ppg, width=110)

peaks_ppg_min, _ = find_peaks(-ppg,  width=110)

peaks_ppg = compoundPeaks(peaks_ppg_min, peaks_ppg_max)

max_amplitude = findMaxAmplitude(ppg[peaks_ppg])

# PascalCase используется для параметра PI(индекса перфузии)

PI = (max_amplitude/amplit_const) * 100

print(PI)

# chartBuilder(time, ppg, peaks_ppg)
