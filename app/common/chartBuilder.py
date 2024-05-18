import matplotlib.pyplot as plt

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
# fix me: надо предложить какой-то другой вариант построение мулти гравиков
    
def multipleChartBuilder(axs, x, y, pick = None, label='', nameX = None, nameY = None, title = None, count = 0): 
    axs[count].plot(x, y, label = label)

    if pick is not None:
        axs[count].plot(x[pick], y[pick], '*')

    axs[count].set_xlabel(nameX)
    axs[count].set_ylabel(nameY)
    axs[count].set_title(title)
    axs[count].grid(True)
    axs[count].legend()
    return multipleChartBuilder
