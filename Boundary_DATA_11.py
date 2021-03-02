import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import shapefile as shp
from netCDF4 import Dataset
import matplotlib.colors as mcolors
from netCDF4 import MFDataset
import imageio
path = ['wrfout_d04_2016-10-31_12_00_00'
,'wrfout_d04_2016-11-01_12_00_00'
,'wrfout_d04_2016-11-02_12_00_00'
,'wrfout_d04_2016-11-03_12_00_00'
,'wrfout_d04_2016-11-04_12_00_00'
,'wrfout_d04_2016-11-05_12_00_00'
,'wrfout_d04_2016-11-06_12_00_00'
,'wrfout_d04_2016-11-07_12_00_00'
,'wrfout_d04_2016-11-08_12_00_00'
,'wrfout_d04_2016-11-09_12_00_00'
,'wrfout_d04_2016-11-10_12_00_00'
,'wrfout_d04_2016-11-11_12_00_00'
,'wrfout_d04_2016-11-12_12_00_00'
,'wrfout_d04_2016-11-13_12_00_00'
,'wrfout_d04_2016-11-14_12_00_00'
,'wrfout_d04_2016-11-15_12_00_00'
,'wrfout_d04_2016-11-16_12_00_00'
,'wrfout_d04_2016-11-17_12_00_00'
,'wrfout_d04_2016-11-18_12_00_00'
,'wrfout_d04_2016-11-19_12_00_00'
,'wrfout_d04_2016-11-20_12_00_00'
,'wrfout_d04_2016-11-21_12_00_00'
,'wrfout_d04_2016-11-22_12_00_00'
,'wrfout_d04_2016-11-23_12_00_00'
,'wrfout_d04_2016-11-24_12_00_00'
,'wrfout_d04_2016-11-25_12_00_00'
,'wrfout_d04_2016-11-26_12_00_00'
,'wrfout_d04_2016-11-27_12_00_00'
,'wrfout_d04_2016-11-28_12_00_00'
,'wrfout_d04_2016-11-29_12_00_00']
#load shapefile

def Taiwan_map():
     sf = shp.Reader('taiwan_district.shp', encoding='ISO-8859-15')

     for shape in sf.shapeRecords():

            l = shape.shape.parts

            len_l = len(l)
            x = [i[0] for i in shape.shape.points[:]]
            y = [i[1] for i in shape.shape.points[:]]
            l.append(len(x))
            for k in range(len_l):

                ax.plot(x[l[k]:l[k + 1]],y[l[k]:l[k + 1]], 'k-')

#fig = plt.figure(figsize = (8.8, 10))
#initial time setting
root_time = False
T = 12
True_T = 8 #UTC+8
Year = 2077
Month = 10
Date = 31
img_path = []
count = 0

for root in path: 
    nc_file = root
    data_nc = Dataset(nc_file)
    PBLH = data_nc.variables['PBLH']
    PBLH_XLONG = data_nc.variables['XLONG']
    PBLH_XLAT = data_nc.variables['XLAT']
    T = 12
    True_T = 8 #UTC+8
    test = 0
    if root_time == True:
        test = 1
        T = 13
        True_T = True_T + 1
    for i in range(25-test):

       
        fig = plt.figure(figsize=(20, 10))
        #fig = plt.figure(figsize = (8.8, 10)) 
    
        cmap = plt.cm.rainbow
        cbar_norm = mpl.colors.Normalize(vmin=100, vmax=1200)
        norm = mcolors.Normalize(vmin=100, vmax=1200)
        
        True_T = str(True_T)
        Year = str(Year)
        Month = str(Month)
        Date = str(Date)
        
        ax = fig.add_subplot(1, 2, 1, projection='3d')
        Taiwan_map()
        title = "NN "+Year+"-"+Month+"-"+Date+" "+ True_T +":00:00 PBLH(m)"
        ax.set_title(title, fontsize=18)
        Max_value = str(int(PBLH[T, :, :].max()))
        Min_value = str(int(PBLH[T, :, :].min()))
        ax.set_xlabel("min = "+Min_value+", "+"max = "+Max_value+" (m)", horizontalalignment='right', fontsize=16)
        ax.set_xlim(119.5, 122.5)
        ax.set_ylim(21.7, 25.5)
        ax.set_zlim(0, 1200)
        cs = ax.plot_surface(PBLH_XLONG[T, :, :], PBLH_XLAT[T, :, :], PBLH[T, :, :], alpha=0.5, cmap=cmap, norm=norm)
        #plt.show()

        ax = fig.add_subplot(1, 2, 2)
        Taiwan_map()
        title = "NN "+Year+"-"+Month+"-"+Date+" "+ True_T +":00:00 PBLH(m)"
        title_graph = "NN "+Year+"-"+Month+"-"+Date+" "+ True_T +"hr PBLH(m).png"
        ax.set_title(title, fontsize=18)
        Max_value = str(int(PBLH[T, :, :].max()))
        Min_value = str(int(PBLH[T, :, :].min()))
        ax.set_xlabel("min = "+Min_value+", "+"max = "+Max_value+" (m)", horizontalalignment='right', fontsize=16)
        ax.set_xlim(119.5, 122.5)
        ax.set_ylim(21.7, 25.5)
        cs2 = ax.contourf(PBLH_XLONG[T, :, :], PBLH_XLAT[T, :, :], PBLH[T, :, :], cmap=cmap, norm=norm)
        fig.colorbar(mpl.cm.ScalarMappable(norm= cbar_norm, cmap=cmap))
    
        fig.savefig(title_graph, dpi=200)
        img_path.append('')
        img_path[count] = title_graph 
        print(title_graph, " finished!")
          
        T = int(T)
        True_T = int(True_T)
        T = T + 1
        True_T = True_T + 1
        count = count + 1
        Year = int(Year)
        Month = int(Month)
        Date = int(Date)
        if True_T>23:
            Date = Date + 1
            True_T = 0
        if Date>29 and Month==2 and True_T==0:
            Month = Month + 1
            Date = 1
        if Date>30 and Month!=2 and (Month==4 or Month==6 or Month==9 or Month==11) and True_T==0:
            Month = Month + 1
            Date = 1
        if Date>31:
            Month = Month + 1
            Date = 1
        if Month>12 :
            Year = Year + 1
            Month = 1
    root_time = True
gif_images = []
for p in img_path:
    gif_images.append(imageio.imread(p))
imageio.mimsave("十一月邊界層高度分布NN.gif",gif_images, duration=0.1, fps=60)
print("Hello World!")
