import matplotlib.pyplot as plt
import numpy as np
from utils import calc_interest
from tqdm import tqdm

x=np.linspace(25,45,10)
x=[round(x_i,1) for x_i in x]
for i in range(10):
    print(x[i])
    calc_interest(x[i],107,7)
#y=[calc_interest(x_i,107,7) for x_i in x]
#plt.plot(x,y)