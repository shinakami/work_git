import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import time as ti
import pandas as pd
import gc
from scipy import stats
import random as rd
from matplotlib.font_manager import FontProperties
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import scipy as sp
from scipy import interpolate
import seaborn as sns
from operator import itemgetter, attrgetter
from win32.win32api import GetSystemMetrics

font = FontProperties(fname=r'C:/Users/user/Anaconda3/Lib/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans.ttc')

data = "Z_velocity_akima.csv"
file = pd.read_csv(data)

data2 = "Guanshan_Saturation.csv"
file2 = pd.read_csv(data2)

x = file2["SINIT"]

y = file["Z_Darcy"]

plt.ylim(round(y.min(), 2), round(y.max(), 2))
y_ticks = np.linspace(round(y.min(), 2), round(y.max(), 2), 10)
plt.yticks(y_ticks)
plt.xlabel("Saturation", fontproperties=font, fontsize=20)
plt.ylabel("q$_{z}$ (m/d)", fontproperties=font, fontsize=20)
plt.scatter(x,y)


plt.show()

fig, ax = plt.subplots()
file["Z_Darcy"].plot.kde()
file["Z_Darcy"].plot.hist(bins=y_ticks, grid=False, rwidth=1, density=True, edgecolor="black")
std = round(np.std(file["Z_Darcy"]),5)
mean = round(np.mean(file["Z_Darcy"]),5)
str_std = str(std)
str_mean = str(mean)
plt.xticks(y_ticks)
plt.xlim(y.min(), y.max())
plt.ylim(0,1)
plt.xlabel("Z_Darcy Flux(m/d)", fontproperties=font, fontsize=10)
plt.text(-0.150, 0.8, "Mean="+str_mean, fontsize=20)
plt.text(-0.150, 0.6, "Std="+str_std, fontsize=20)
plt.tight_layout()
plt.show()

#plt.hist(file["Z_Darcy"], color="green", bins = y_ticks, density=True)
#plt.xticks(y_ticks)
#plt.xlim(y.min(), y.max())
#plt.show()


data3 = "river_hyporheic_z_stats.csv"
file3 = pd.read_csv(data3)

elevation=file3["Z"]
Z_FLUX=file3["Z_Darcy"]

plt.ylim(Z_FLUX.min(), Z_FLUX.max())
y_ticks = np.linspace(Z_FLUX.min(), Z_FLUX.max(), 25)
plt.yticks(y_ticks)
plt.xlabel("elevation(m)", fontproperties=font, fontsize=20)
plt.ylabel("Z_Darcy Flux(m/d)", fontproperties=font, fontsize=20)
plt.scatter(elevation,Z_FLUX)
plt.tight_layout()

plt.show()


space_len=len(elevation)
s=(space_len,2)
data_space=np.zeros(s)

for i in np.arange(0,len(elevation)):
    data_space[i][0]=elevation[i]
    data_space[i][1]=Z_FLUX[i]



data_sort=sorted(data_space, key=itemgetter(0), reverse=True)
ele_sort=np.zeros(space_len)
z_velocity_sort=np.zeros(space_len)
z_velocity_positive_withele=[[0,0]]
z_velocity_negetive_withele=[[0,0]]
p=0
n=0
for i in np.arange(0,len(elevation)):
    ele_sort[i]=data_sort[i][0]
    z_velocity_sort[i]=data_sort[i][1]
    if(data_sort[i][1]<0):
        z_velocity_negetive_withele[n][0]=data_sort[i][0]
        z_velocity_negetive_withele[n][1]=data_sort[i][1]
        z_velocity_negetive_withele.append([0,0])
        
        n=n+1
    elif(data_sort[i][1]>0):
        z_velocity_positive_withele[p][0]=data_sort[i][0]
        z_velocity_positive_withele[p][1]=data_sort[i][1]
        z_velocity_positive_withele.append([0,0])
        
        p=p+1




plt.ylim(z_velocity_sort.min(), z_velocity_sort.max())
y_ticks = np.linspace(z_velocity_sort.min(), z_velocity_sort.max(), 25)
plt.yticks(y_ticks)
plt.xlabel("elevation(m)", fontproperties=font, fontsize=20)
plt.ylabel("Z_Darcy Flux(m/d)", fontproperties=font, fontsize=20)
plt.scatter(ele_sort,z_velocity_sort, color="green")
plt.tight_layout()

plt.show()

ele_level=np.arange(ele_sort.min(), ele_sort.max(), 10)
ele_level=sorted(ele_level, reverse=True)

std_space=np.zeros(len(ele_level))
corr_space=np.zeros(len(ele_level))
average_space=np.zeros(len(ele_level))
g=0
a=0
z_velocity_local=[0]
for i in np.arange(0,len(ele_level)-1):
    a=0
    for x in np.arange(0, space_len):
        ele=ele_sort[x]
        if(ele<=ele_level[i] and ele>=ele_level[i+1]):
            z_velocity_local[a]=z_velocity_sort[x]
            z_velocity_local.append(0)
            a=a+1
    
    std_space[g]=round(np.std(z_velocity_local),12)
    average_space[g]=np.average(z_velocity_local)
    corr_space[g]=std_space[g]/average_space[g]
    g=g+1
    z_velocity_local=[0]


depth=np.zeros(len(ele_level))
for i in np.arange(0, len(ele_level)):
    depth[i]=abs(ele_level[i]-ele_level[0])


##全河道下方含水層
fig = plt.figure(figsize = (9,8))
ax = fig.add_subplot(111)
plt.ylim(corr_space.min(), corr_space.max())
y_ticks = np.linspace(corr_space.min(), corr_space.max(), 25)
plt.yticks(y_ticks)
plt.xlabel("Depth(m)", fontproperties=font, fontsize=20)
plt.ylabel("Coefficient of variation", fontproperties=font, fontsize=20)
plt.scatter(depth,corr_space, color="red")
plt.plot(depth,corr_space, color="green")
plt.tight_layout()

plt.show()


std_space_minus=np.zeros(len(ele_level))
std_space_plus=np.zeros(len(ele_level))
average_space_minus=np.zeros(len(ele_level))
average_space_plus=np.zeros(len(ele_level))
corr_space_minus=np.zeros(len(ele_level))
corr_space_plus=np.zeros(len(ele_level))
g=0
a=0
z_velocity_local_minus=[0]
z_velocity_local_plus=[0]
for i in np.arange(0,len(ele_level)-1):
    a=0
    for x in np.arange(0, len(z_velocity_negetive_withele)):
        ele=ele_sort[x]
        if(ele<=ele_level[i] and ele>=ele_level[i+1]):
            z_velocity_local_minus[a]=z_velocity_negetive_withele[x][1]
            z_velocity_local_minus.append(0)
            a=a+1
    
    std_space_minus[g]=round(np.std(z_velocity_local_minus),12)
    average_space_minus[g]=abs(np.average(z_velocity_local_minus))
    corr_space_minus[g]=std_space_minus[g]/average_space_minus[g]
    g=g+1
    z_velocity_local_minus=[0]



g=0
a=0
for i in np.arange(0,len(ele_level)-1):
    a=0
    for x in np.arange(0, len(z_velocity_positive_withele)):
        ele=ele_sort[x]
        if(ele<=ele_level[i] and ele>=ele_level[i+1]):
            z_velocity_local_plus[a]=z_velocity_positive_withele[x][1]
            z_velocity_local_plus.append(0)
            a=a+1
    
    std_space_plus[g]=round(np.std(z_velocity_local_plus),12)
    average_space_plus[g]=np.average(z_velocity_local_plus)
    corr_space_plus[g]=std_space_plus[g]/average_space_plus[g]
    g=g+1
    z_velocity_local_plus=[0]




    
fig = plt.figure(figsize = (9,8))
ax = fig.add_subplot(111)
plt.ylim(corr_space.min(), corr_space.max())
y_ticks = np.linspace(corr_space.min(), corr_space.max(), 25)
plt.yticks(y_ticks)
plt.xlabel("Depth(m)", fontproperties=font, fontsize=20)
plt.ylabel("Activity(+Vz)", fontproperties=font, fontsize=20)
plt.scatter(depth,corr_space_plus, color="red")
plt.plot(depth,corr_space_plus, color="blue")
plt.tight_layout()

plt.show()

fig = plt.figure(figsize = (9,8))
ax = fig.add_subplot(111)
plt.ylim(corr_space.min(), corr_space.max())
y_ticks = np.linspace(corr_space.min(), corr_space.max(), 25)
plt.yticks(y_ticks)
plt.xlabel("Depth(m)", fontproperties=font, fontsize=20)
plt.ylabel("Activity(-Vz)", fontproperties=font, fontsize=20)
plt.scatter(depth,corr_space_minus, color="red")
plt.plot(depth,corr_space_minus, color="blue")
plt.tight_layout()

plt.show()        

fig = plt.figure(figsize = (9,8))
ax = fig.add_subplot(111)
plt.ylim(corr_space.min(), corr_space.max())
y_ticks = np.linspace(corr_space.min(), corr_space.max(), 25)
plt.yticks(y_ticks)
plt.xlabel("Depth(m)", fontproperties=font, fontsize=20)
plt.ylabel("Activity", fontproperties=font, fontsize=20)
plt.scatter(depth,corr_space_plus, color="black")
P_line=plt.plot(depth,corr_space_plus, color="blue", label="+Vz")
plt.scatter(depth,corr_space_minus, color="black")
N_line=plt.plot(depth,corr_space_minus, color="green", label="-Vz")
plt.scatter(depth,corr_space, color="black")
T_line=plt.plot(depth,corr_space, color="red", label="Total Vz")
plt.legend(title="Activity of -Vz&+Vz")
plt.tight_layout()

plt.show()       




Slice=file3["Slice"]            
         

space_len_slice=len(Slice)
s=(space_len_slice,2)
data_space_slice=np.zeros(s)

for i in np.arange(0,len(Slice)):
    data_space_slice[i][0]=Slice[i]
    data_space_slice[i][1]=Z_FLUX[i]


z_velocity_positive_withSlice=[[0,0]]
z_velocity_negetive_withSlice=[[0,0]]
p=0
n=0
for i in np.arange(0,len(Slice)):
    if(data_space_slice[i][1]<0):
        z_velocity_negetive_withSlice[n][0]=data_space_slice[i][0]
        z_velocity_negetive_withSlice[n][1]=data_space_slice[i][1]
        z_velocity_negetive_withSlice.append([0,0])
        n=n+1
    elif(data_space_slice[i][1]>0):
        z_velocity_positive_withSlice[p][0]=data_space_slice[i][0]
        z_velocity_positive_withSlice[p][1]=data_space_slice[i][1]
        z_velocity_positive_withSlice.append([0,0])
        p=p+1

std_space_Slice=np.zeros(16)
corr_space_Slice=np.zeros(16)
average_space_Slice=np.zeros(16)
z_velocity_local_Slice=[]
g=0 
S=0
for i in np.arange(1,Slice.max()+1):
    for x in np.arange(0, len(Slice)):
        S=int(data_space_slice[x][0])
        z_velocity_local_Slice.append(0)
        if(S==i):
            z_velocity_local_Slice[x]=data_space_slice[x][1]
    std_space_Slice[i-1]=np.std(z_velocity_local_Slice)
    average_space_Slice[i-1]=np.average(z_velocity_local_Slice)
    corr_space_Slice[i-1]=std_space_Slice[i-1]/average_space_Slice[i-1]
    z_velocity_local_Slice=[0]


Slice_num=np.arange(1,Slice.max()+1)

fig = plt.figure(figsize = (9,8))
ax = fig.add_subplot(111)
plt.ylim(corr_space_Slice.min(), corr_space_Slice.max())
x_ticks = np.linspace(Slice_num.min(), Slice_num.max(), 16)
y_ticks = np.linspace(round(corr_space_Slice.min(), 2), round(corr_space_Slice.max(), 2), 11)
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.xlabel("Slice", fontproperties=font, fontsize=20)
plt.ylabel("coefficient of variation of "+"q$_{z}$", fontproperties=font, fontsize=20)
plt.scatter(Slice_num,corr_space_Slice, color="black")
plt.plot(Slice_num,corr_space_Slice, color="blue", label="CV of Vz")
plt.tight_layout()

plt.show()

fig = plt.figure(figsize = (9,8))
ax = fig.add_subplot(111)
plt.ylim(average_space_Slice.min(), average_space_Slice.max())
x_ticks = np.linspace(Slice_num.min(), Slice_num.max(), 16)
y_ticks = np.linspace(average_space_Slice.min(), average_space_Slice.max(), 10)
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.xlabel("Slice", fontproperties=font, fontsize=20)
plt.ylabel("Mean of "+"q$_{z}$", fontproperties=font, fontsize=20)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.scatter(Slice_num,average_space_Slice, color="black")
plt.plot(Slice_num,average_space_Slice, color="green", label="Average of Vz")
plt.tight_layout()

plt.show()


fig = plt.figure(figsize = (9,8))
ax = fig.add_subplot(111)
plt.ylim(std_space_Slice.min(), std_space_Slice.max())
x_ticks = np.linspace(Slice_num.min(), Slice_num.max(), 16)
y_ticks = np.linspace(std_space_Slice.min(), std_space_Slice.max(), 10)
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.xlabel("Slice", fontproperties=font, fontsize=20)
plt.ylabel("Std of "+"q$_{z}$", fontproperties=font, fontsize=20)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.scatter(Slice_num,std_space_Slice, color="black")
plt.plot(Slice_num,std_space_Slice, color="green", label="Std of Vz")
plt.tight_layout()

plt.show()

fig = plt.figure(figsize = (9,8))
ax = fig.add_subplot(111)
plt.ylim(average_space_Slice.min()*10**5, corr_space_Slice.max())
x_ticks = np.linspace(Slice_num.min(), Slice_num.max(), 16)
y_ticks = np.linspace(average_space_Slice.min()*10**5, corr_space_Slice.max(), 25)
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.xlabel("Slice", fontproperties=font, fontsize=20)
plt.ylabel("Value", fontproperties=font, fontsize=20)
plt.scatter(Slice_num,average_space_Slice*10**5, color="black")
plt.plot(Slice_num,average_space_Slice*10**5, color="green", label="Average(1E5) of Vz")
plt.scatter(Slice_num,corr_space_Slice, color="black")
plt.plot(Slice_num,corr_space_Slice, color="blue", label="CV of Vz")
plt.legend(title="Parameter Index")
plt.tight_layout()

plt.show()

std_space_Slice_negetive=np.zeros(16)
corr_space_Slice_negetive=np.zeros(16)
average_space_Slice_negetive=np.zeros(16)

std_space_Slice_positive=np.zeros(16)
corr_space_Slice_positive=np.zeros(16)
average_space_Slice_positive=np.zeros(16)

z_velocity_local_Slice_negetive=[]
z_velocity_local_Slice_positive=[]
g=0
S=0
for i in np.arange(1,Slice.max()+1):
    for x in np.arange(0, len(z_velocity_negetive_withSlice)):
        S=int(data_space_slice[x][0])
        z_velocity_local_Slice_negetive.append(0)
        if(S==i):
            z_velocity_local_Slice_negetive[x]=z_velocity_negetive_withSlice[x][1]

    std_space_Slice_negetive[i-1]=np.std(z_velocity_local_Slice)
    average_space_Slice_negetive[i-1]=np.average(z_velocity_local_Slice_negetive)
    corr_space_Slice_negetive[i-1]=std_space_Slice_negetive[i-1]/average_space_Slice_negetive[i-1]
    z_velocity_local_Slice_negetive=[0]
g=0
S=0
for i in np.arange(1,Slice.max()+1):
    for x in np.arange(0, len(z_velocity_positive_withSlice)):
        S=int(data_space_slice[x][0])
        z_velocity_local_Slice_positive.append(0)
        if(S==i):
            z_velocity_local_Slice_positive[x]=z_velocity_positive_withSlice[x][1]

    std_space_Slice_positive[i-1]=np.std(z_velocity_local_Slice_positive)
    average_space_Slice_positive[i-1]=np.average(z_velocity_local_Slice_positive)
    corr_space_Slice_positive[i-1]=std_space_Slice_positive[i-1]/average_space_Slice_positive[i-1]
    z_velocity_local_Slice_positive=[0]

print(corr_space_Slice_positive)
print(corr_space_Slice_negetive)
