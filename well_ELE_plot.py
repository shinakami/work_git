import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import time as ti
import pandas as pd
from scipy import stats
import random as rd
from matplotlib.font_manager import FontProperties
from scipy import interpolate
font = FontProperties(fname=r'C:/Users/user/Anaconda3/Lib/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans.ttc')


def linear_regression(x,y):
  x=np.concatenate((np.ones((x.shape[0],1)),x[:,np.newaxis]),axis=1)
  y=y[:,np.newaxis]
  beta=np.matmul(np.matmul(np.linalg.inv(np.matmul(x.T,x)),x.T),y)
  return beta
pass


path = 'well.csv'
file = pd.read_csv(path)
print(file['level'])
print(file['ELE'])
print(len(file['level']))

by_hand = linear_regression(file['ELE'], file['level'])
print(by_hand[0])
print(by_hand[1])
dis = by_hand[0]
m = by_hand[1]
str_dis=str(dis)
str_m=str(m)
xs = np.linspace(0,150, 5)
ys = dis+m*xs
plt.xlabel("地表高程(m)", fontproperties=font, fontsize=15)
plt.ylabel("水頭(m)", fontproperties=font, fontsize=15)
plt.plot(xs ,ys, color='green')
plt.scatter(file['ELE'], file['level'], color='red' )
plt.text(10, 100, "水頭=" + str_m + "高程" + str_dis + "(單位:公尺)" , fontproperties=font, fontsize=10)
plt.show()