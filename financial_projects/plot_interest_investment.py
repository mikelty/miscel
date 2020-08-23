import numpy as np
from utils import calc_interest
import matplotlib.pyplot as plt
from matplotlib.pylab import style

def plot_varying_funds():
    style.use('ggplot')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    x=np.linspace(25,45,10)
    x=[round(x_i,1) for x_i in x]
    y=[calc_interest(x_i,107,7) for x_i in x]
    plt.plot(x,y)
    plt.xlabel('本金')
    plt.ylabel('周期利率（百分比）')
    plt.legend()
    plt.show()