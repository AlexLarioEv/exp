import numpy as np

from scipy.signal import find_peaks
from service.getOpenSignal import clean_signal, time, fs as fs_signal
from breath import resperator_signal, time_res, peaks_res, max_peaks_res, fs as fs_res
from common import getTimeSignal, splitSignal, multipleChartBuilder, chartBuilder, filterButter,fftSignal

signals = splitSignal(clean_signal, peaks_res)
signals_res = splitSignal(resperator_signal, peaks_res)

dataBreath = {'inhalationTime': [],'inhalationFrequency': [], 'exhalationTime':[], 'exhalationFrequency': []}

# нахождение фаз вдоха и выдоха


for i in signals_res:
    res_puls_signal =  filterButter(signals[i], 5, fs_signal)
    freg_mag_res_puls, freq_scale_res_puls = fftSignal(res_puls_signal, getTimeSignal(res_puls_signal, fs_signal))
    peaks_puls, _ = find_peaks(freg_mag_res_puls)
    max_peak_puls = peaks_puls[np.argmax(freg_mag_res_puls[peaks_puls])]

    timeBreathPhase = getTimeSignal(signals_res[i], fs_res)[-1]
    freq_puls = freq_scale_res_puls[max_peak_puls]


    # chartBuilder(freq_scale_res_puls, freg_mag_res_puls, max_peak_puls)

    if  peaks_res[i] in max_peaks_res:
        print('inhalation phase time', timeBreathPhase) 
        # chartBuilder(getTimeSignal(signals_res[i], fs_res), signals_res[i], title='фаза вдоха')

        print('inhalation phase pulse frequency', freq_puls)
        # chartBuilder(getTimeSignal(res_puls_signal, fs_signal), res_puls_signal, title='фаза вдоха', label='пульс на вдохе')

        if (i !=0 or timeBreathPhase > 1.5 ) and (i != len(signals_res)-1 or timeBreathPhase > 1.5):
            dataBreath['inhalationTime'].append(timeBreathPhase)
            dataBreath['inhalationFrequency'].append(freq_puls)
 
        continue
    
    print('exhalation phase time', timeBreathPhase)
    # chartBuilder(getTimeSignal(signals_res[i], fs_res), signals_res[i], title='фаза выдоха')

    print('exhalation phase pulse frequency', freq_puls)
    # chartBuilder(getTimeSignal(res_puls_signal, fs_signal), res_puls_signal, title='фаза выдоха', label='пульс на выдохе')
    if (i !=0 or timeBreathPhase > 1.5 ) and (i != len(signals_res)-1 or timeBreathPhase > 1):
        dataBreath['exhalationTime'].append(timeBreathPhase)
        dataBreath['exhalationFrequency'].append(freq_puls)

# dif_resp_signal = np.diff(resperator_signal)

# min_peaks_res_diff , _ = find_peaks(-dif_resp_signal)

# min_peaks_res_diff_norm=sorted([*min_peaks_res_diff, *min_peaks_res])


# j = 0

# for i in min_peaks_res_diff:
#    res_pause = min_peaks_res[j] - min_peaks_res_diff[j]
#    print(res_pause/1000)
#    j+=1


# # res_pause = min_peaks_res[2] - min_peaks_res_diff[3]
# # print(res_pause/1000)

# chartBuilder(getTimeSignal(dif_resp_signal, fs_signal), dif_resp_signal, min_peaks_res_diff_norm, title='первая производная дых. волны')
# chartBuilder(time_res, resperator_signal, min_peaks_res_diff_norm)