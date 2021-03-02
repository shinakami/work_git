import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import time as ti
import pandas as pd
import scipy as sp
import random as rd
from matplotlib.font_manager import FontProperties
font = 'Simsun'

sample_test=0
loop=True
n=500
data_test=np.zeros(n)
sample_av=0
sample_range=np.arange(1,n+1)
random_array=np.zeros(1)
x=0
time=0

for test in sample_range:
    while loop==True:
        a=rd.randint(1,6)
        sample_test=sample_test+1
        time=time+1      
        if a==5:
            random_array[x]=time
            random_array=np.append(random_array, 0)
            x=x+1
            sample_av=sample_test/test
            data_test[test-1]=sample_av
            time=0
            print("第",test,"次採樣=","平均第",sample_av,"次骰到5")
            break
        pass
    pass
pass
#print("最終採樣平均=",sample_av)

plt.xticks(np.arange(0, 12, 1))
plt.ylim(0, 1)
plt.xlim(0, 12)
sample_mean=np.mean(random_array)
plt.text(0.5, 0.8, "採樣平均值=", fontproperties=font, fontsize=15, color='blue')
plt.text(3.5, 0.8, sample_mean, fontproperties=font, fontsize=10, color='black')
plt.hist(random_array, histtype='step', color = "black" ,bins = np.arange(0,12,0.1), density=True, cumulative=True)
plt.show()


theorical_val=np.linspace(6, 6, n)
plt.xlim(0,n)
plt.ylim(0,10)
plt.xticks(np.arange(0, n, 50))
plt.yticks(np.arange(0, 10, 1))
plt.xlabel("採樣次數", fontproperties=font, fontsize=15)
plt.ylabel("平均骰到5的次數", fontproperties=font, fontsize=15)
plt.grid(True)
plt.plot(sample_range, theorical_val, color="red", linewidth=3.0)
plt.plot(sample_range, data_test, color="blue")
plt.text(350, 4.5, "- 理論平均值", fontproperties=font, fontsize=15, color='red')
plt.text(350, 3, "- 採樣平均值", fontproperties=font, fontsize=15, color='blue')
plt.show()

samples=20
data_sample=np.zeros(samples)
sample_av_array=np.zeros(samples)
sample_test=0
sample_av=0
for time in np.arange(1, samples+1):
    for test in sample_range:
        while loop==True:
            dice=rd.randint(1,6)
            sample_test=sample_test+1
            if dice==5:
                sample_av=sample_test/test
                break
            pass
        pass
    pass
    print("第", time, "個抽到5的樣本平均次數=", sample_av)
    data_sample[time-1]=sample_av
    total_av=sum(data_sample)
    sample_av_array[time-1]=total_av/time
    sample_av=0
    test=0
    sample_test=0
pass

total_sample=sum(data_sample)
Mean=total_sample/samples
print("樣本平均值之平均值=", Mean)

theorical_val=np.linspace(6, 6, samples)
plt.xlim(0,samples)
plt.ylim(0,10)
plt.xticks(np.arange(0, samples, 5))
plt.yticks(np.arange(0, 10, 1))
plt.xlabel("樣本數", fontproperties=font, fontsize=15)
plt.ylabel("平均骰到5的次數", fontproperties=font, fontsize=15)
plt.grid(True)
plt.plot(np.arange(0, samples), theorical_val, color="red", linewidth=5.0)
plt.plot(np.arange(0, samples), sample_av_array,"k--", linewidth=3.0)
plt.show()

fig=plt.figure()
ax1=fig.add_subplot(2, 1, 1)
ax2=fig.add_subplot(2, 1, 2)

ax1.set_xticks(np.arange(0, 12, 1))
ax1.set_xlim(0, 12)
ax1.set_ylim(0, 1)
ax1.set_xlabel("抽中數字5之次數", fontproperties=font, fontsize=15)
ax1.text(0.5, 0.8, "採樣平均值=", fontproperties=font, fontsize=15, color='blue')
ax1.text(3.5, 0.8, sample_mean, fontproperties=font, fontsize=10, color='black')
ax1.hist(random_array, histtype='step', color = "black" ,bins = np.arange(0,12,0.1), density=True, cumulative=True)
ax1.hist(random_array, color = "green", edgecolor = "black" ,bins = np.arange(0,12,1), density=True)

theorical_val=np.linspace(6, 6, n)
ax2.set_ylim(0, 10)
ax2.set_xlim(0, n)
ax2.set_xlabel("採樣次數", fontproperties=font, fontsize=15)
ax2.set_ylabel("平均骰到5的次數", fontproperties=font, fontsize=15)
ax2.grid(True)
ax2.plot(sample_range, theorical_val, color="red", linewidth=3.0)
ax2.plot(sample_range, data_test, color="blue")
ax2.text(350, 4.5, "- 理論平均值", fontproperties=font, fontsize=15, color='red')
ax2.text(350, 3, "- 採樣平均值", fontproperties=font, fontsize=15, color='blue')

plt.tight_layout()
plt.show()