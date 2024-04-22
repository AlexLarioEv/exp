import matplotlib.pyplot as plt

from pulse import puls_signal, fs, time
from service import getSignal
from common import  chartBuilder




print(puls_signal.std())
plt.boxplot(puls_signal)
plt.show()
