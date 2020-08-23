
import matplotlib.pyplot as plt
import numpy as np
import scipy

from matplotlib.pylab import style
style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
噪音=1
焊接点损耗=50
损耗区域=.2
全部焊接点=[5,11]


x=np.linspace(0,20,100)
y=-x-np.random.uniform(low=-噪音/2.,high=噪音/2.,size=(len(x)))
print(y)
for 焊接点 in 全部焊接点:
    for i,p in enumerate(x):
        dist=abs(焊接点-p)
        if dist<损耗区域/2.:
            y[i]+=(1-dist)*焊接点损耗

plt.plot(x,y,label="电缆甲")
plt.legend()
plt.title("焊接损耗情况")
plt.xlabel("距离（米）")
plt.ylabel("损耗值（dB）")
plt.show()