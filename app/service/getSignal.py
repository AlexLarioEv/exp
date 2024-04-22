import pandas as pd
import numpy as np

def getSignal(path, name):
    try:
        data = pd.read_csv(path, sep='\t', names=[name])
        signal = data[name]
        return signal
    except:
        print('Error: requesting data')
        print('Enter the path')
        path = input()
        return getSignal(path, name)
