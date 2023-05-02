import pandas as pd
import numpy as np

from transformSIgnals import decimateSignal

def getSignal(path, name):
    data = pd.read_csv(path, sep='\t', names=[name])
    signal = data[name]

    return signal
