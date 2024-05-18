import numpy as np

from scipy.signal import find_peaks
from getOpenSignal import clean_signal, time, fs as fs_signal
from breath import resperator_signal, time_res, peaks_res, fs as fs_res
from common import getTimeSignal, splitSignal, multipleChartBuilder, chartBuilder, filterButter,fftSignal

signals = splitSignal(clean_signal, peaks_res)
signals_res = splitSignal(resperator_signal, peaks_res)

# нахождение фаз вдоха и выдоха

freg_mag_puls, freq_scale_puls = fftSignal(clean_signal, time)
peaks_puls, _ = find_peaks(freg_mag_puls)
max_peak_puls = peaks_puls[np.argmax(freg_mag_puls[peaks_puls])]
# chartBuilder(freq_scale_puls, freg_mag_puls, max_peak_puls)

for i in signals_res:
    res_puls_signal =  filterButter(signals[i], 5, fs_signal)
    freg_mag_res_puls, freq_scale_res_puls = fftSignal(res_puls_signal, getTimeSignal(res_puls_signal, fs_signal))
    peaks_puls, _ = find_peaks(freg_mag_res_puls)
    max_peak_puls = peaks_puls[np.argmax(freg_mag_res_puls[peaks_puls])]

    # chartBuilder(freq_scale_res_puls, freg_mag_res_puls, max_peak_puls)
    
    if  peaks_res[i] in peaks_res:
        print('inhalation phase time', getTimeSignal(signals_res[i], fs_res)[-1]) 
        # chartBuilder(getTimeSignal(signals_res[i], fs_res), signals_res[i], title='фаза вдоха')

        print('inhalation phase pulse frequency', freq_scale_res_puls[max_peak_puls])
        chartBuilder(getTimeSignal(res_puls_signal, fs_signal), res_puls_signal, title='фаза вдоха', label='пульс на вдохе')
        continue
    
    print('exhalation phase time', getTimeSignal(signals_res[i], fs_res)[-1]) 
    # chartBuilder(getTimeSignal(signals_res[i], fs_res), signals_res[i], title='фаза выдоха')

    print('exhalation phase pulse frequency', freq_scale_res_puls[max_peak_puls])
    chartBuilder(getTimeSignal(res_puls_signal, fs_signal), res_puls_signal, title='фаза выдоха', label='пульс на выдохе')

