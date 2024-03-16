import matplotlib.pyplot as plt
import matplotlib

def chartBuilder(x, y, pick = None, title = '', label = '', nameX = 'ось X', nameY = 'ось Y'):
    plt.plot(x, y , label=label )
    if pick is not None :
        plt.plot(x[pick], y[pick], '*' )
    plt.title(label=title, fontsize=17)
    plt.xlabel(nameX, fontsize=15)
    plt.ylabel(nameY, fontsize=15)
    plt.grid(True)
    plt.legend()
    plt.show()

# Info: Передаем в axs второй выхождной параметр plt.subplots

def multipleChartBuilder(axs, x, y, pick = None, label='',nameX = 'ось X',nameY = 'ось Y', count = 0): 
    axs[count].plot(x, y, label=label)

    if pick is not None:
        axs[count].plot(x[pick], y[pick], '*')

    axs[count].set_xlabel(nameX)
    axs[count].set_ylabel(nameY)
    axs[count].set_title('Name')
    axs[count].grid(True)
    axs[count].legend()
    return multipleChartBuilder

def wrappermultChartBuilder(fn): 
    fig, axs = plt.subplots(2, 1, figsize=(8, 6))
    fn(axs, ...)
    plt.tight_layout()
    plt.show()
    

# График исходного сигнала и сплайна