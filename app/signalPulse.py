from service import getSignal
from common import decimateSignal, getTimeSignal

from constants import fs

# TODO: нет DATA9

signal = getSignal('./db/DATA3.csv', 'pulse_wave')
signal, fs = decimateSignal(signal, fs, 100)
time = getTimeSignal(signal, fs)
