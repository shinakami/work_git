import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import netCDF4
import xarray as xr
from netCDF4 import Dataset
from netCDF4 import MFDataset
import matplotlib.colors as mcolors
import os
os.system('cls')
path_csv = 'F:\\Air_station\\air_data.csv'
file_csv = pd.read_csv(path_csv, encoding='big5')
stat_lon = file_csv['經度']
stat_lat = file_csv['緯度']
stat_code = 17
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def create_dir(file_csv):
    for i in range(len(file_csv['測站名稱'])):
        create_dir = file_csv['測站名稱'][i]
        if not os.path.exists(create_dir):
            os.mkdir(create_dir)
        else:
            print(create_dir + '已經建立！')
#create_dir(file_csv)

def find_dir(dir):
    fds=os.listdir(dir)
    path = []
    i = 0 
    for fd in fds:
        path.append('')
        full_path=os.path.join(dir,fd)
        path[i] = full_path
        i = i + 1
    return path
file_nc_path = 'F:\\Air_station\\nc'
file_nc_path_geo = 'F:\\Air_station\\nc_geo'
nc_root = find_dir(file_nc_path)
nc_geo_root = find_dir(file_nc_path_geo)
nc_geo = nc_geo_root[0]
path_stat_csv = ['Kannon_1_airQstat.csv','Kannon_4_airQstat.csv'
,'Kannon_7_airQstat.csv','Kannon_10_airQstat.csv']
month = ['2016_1月','2016_4月','2016_7月','2016_10月']
time_line = np.arange(0, 24, 1)
d = 1
Janu = []
April = []
July = []
Oct = []
Janu_fix = []
April_fix = []
July_fix = []
Oct_fix = []
year = '2016'
s = 0
for i in range(31):
    d = str(d)
    Janu += ['']
    July += ['']
    Oct += ['']
    Janu[i] = year + '/' + str(1) + '/' + d
    if int(d) <= 30:
        April += ['']
        April[i] = year + '/' + str(4) + '/' + d
    July[i] = year + '/' + str(7) + '/' + d
    Oct[i] = year + '/' + str(10) + '/' + d
    for t in time_line:
        Janu_fix.append('')
        July_fix.append('')
        Oct_fix.append('')
        Janu_fix[s] = Janu[i]
        if int(d) <= 30:
            April_fix.append('')
            April_fix[s] = April[i]
        July_fix[s] = July[i]
        Oct_fix[s] = Oct[i]
        s = s + 1
    d = int(d)
    d = d + 1 




for f in range(len(path_stat_csv)):
    os.system('cls')
    if f == 0:
        month_setting = Janu
        month_fixing = Janu_fix
    elif f == 1:
        month_setting = April
        month_fixing = April_fix
    elif f == 2:
        month_setting = July
        month_fixing = July_fix
    elif f == 3:
        month_setting = Oct
        month_fixing = Oct_fix
   
    file_stat = pd.read_csv(path_stat_csv[f])
    nc_file = nc_root[f]
    for i in time_line:
        i = str(i)
        #Data cleaning
        for x in range(len(file_stat[i])):
            if file_stat[i][x] == '':
                file_stat[i][x] = np.nan
            if isinstance(file_stat[i][x], str) == True and is_number(file_stat[i][x]) == True:
                file_stat[i][x] = np.float64(file_stat[i][x])     
            elif isinstance(file_stat[i][x], str) == True and is_number(file_stat[i][x]) == False:
                st = file_stat[i][x]
                st = [s for s in st.split('*') if s.isdigit()]
                if len(st) > 0:
                    file_stat[i][x] = np.float64(st[0])
                else:
                    file_stat[i][x] = np.nan
            if file_stat[i][x] < 0:
                file_stat[i][x] = abs(file_stat[i][x])
    os.system('cls')
    SO2_stat = []
    NO2_stat = []
    NOX_stat = []
    NO_stat = []
    O3_stat = []
    NMHC_stat = []
    PM10_stat = []
    PM25_stat = []

    SO2_day = []
    NO2_day = []
    NOX_day = []
    NO_day =[]
    O3_day = []
    NMHC_day = []
    PM10_day = []
    PM25_day = []

    SO2_pos = []
    NO2_pos = []
    NOX_pos = []
    NO_pos =[]
    O3_pos = []
    NMHC_pos = []
    PM10_pos = []
    PM25_pos = []

    SO2_count = 0
    NO2_count = 0
    NOX_count = 0
    NO_count = 0
    O3_count = 0
    NMHC_count = 0
    PM10_count = 0
    PM25_count = 0
             
    for L in range(len(file_stat['測項(單位)'])):
    
        if file_stat['測項(單位)'][L] == '二氧化硫 SO2 (ppb)':
            for i in time_line:
                i = str(i)
                SO2_stat.append(0)
                SO2_day += ['']
                SO2_pos += ['']
                SO2_pos[SO2_count] = file_stat['測站'][L]
                SO2_day[SO2_count] = file_stat['監測日期'][L]
                SO2_stat[SO2_count] = file_stat[i][L]
                SO2_count = SO2_count + 1
        elif file_stat['測項(單位)'][L] == '二氧化氮 NO2 (ppb)':
            for i in time_line:
                i = str(i)
                NO2_stat.append(0)
                NO2_day += ['']
                NO2_pos += ['']
                NO2_pos[NO2_count] = file_stat['測站'][L]
                NO2_day[NO2_count] = file_stat['監測日期'][L]
                NO2_stat[NO2_count] = file_stat[i][L]
                NO2_count = NO2_count + 1
        elif file_stat['測項(單位)'][L] == '氮氧化物 NOx (ppb)':
            for i in time_line:
                i = str(i)
                NOX_stat.append(0)
                NOX_day += ['']
                NOX_pos += ['']
                NOX_pos[NOX_count] = file_stat['測站'][L]
                NOX_day[NOX_count] = file_stat['監測日期'][L]
                NOX_stat[NOX_count] = file_stat[i][L]
                NOX_count = NOX_count + 1
        elif file_stat['測項(單位)'][L] == '一氧化氮 NO (ppb)':    
            for i in time_line:
                i = str(i)
                NO_stat.append(0)
                NO_day += ['']
                NO_pos += ['']
                NO_pos[NO_count] = file_stat['測站'][L]
                NO_day[NO_count] = file_stat['監測日期'][L]
                NO_stat[NO_count] = file_stat[i][L]
                NO_count = NO_count + 1
        elif file_stat['測項(單位)'][L] == '臭氧 O3 (ppb)':
            for i in time_line:
                i = str(i)
                O3_stat.append(0)
                O3_day += ['']
                O3_pos += ['']
                O3_pos[O3_count] = file_stat['測站'][L]
                O3_day[O3_count] = file_stat['監測日期'][L]
                O3_stat[O3_count] = file_stat[i][L]
                O3_count = O3_count + 1
        elif file_stat['測項(單位)'][L] == '懸浮微粒 PM 10  (μg/m 3 )':
            for i in time_line:
                i = str(i)
                PM10_stat.append(0)
                PM10_day += ['']
                PM10_pos += ['']
                PM10_pos[PM10_count] = file_stat['測站'][L]
                PM10_day[PM10_count] = file_stat['監測日期'][L]
                PM10_stat[PM10_count] = file_stat[i][L]
                PM10_count = PM10_count + 1
        elif file_stat['測項(單位)'][L] == '細懸浮微粒 PM 2.5  (μg/m 3 )':
            for i in time_line:
                i = str(i)
                PM25_stat.append(0)
                PM25_day += ['']
                PM25_pos += ['']
                PM25_pos[PM25_count] = file_stat['測站'][L]
                PM25_day[PM25_count] = file_stat['監測日期'][L]
                PM25_stat[PM25_count] = file_stat[i][L]
                PM25_count = PM25_count + 1
        elif file_stat['測項(單位)'][L] == '非甲烷碳氫化合物 NMHC (ppm)':
            for i in time_line:
                i = str(i)
                NMHC_stat.append(0)
                NMHC_day += ['']
                NMHC_pos += ['']
                NMHC_pos[NMHC_count] = file_stat['測站'][L]
                NMHC_day[NMHC_count] = file_stat['監測日期'][L]
                NMHC_stat[NMHC_count] = file_stat[i][L]
                NMHC_count = NMHC_count + 1

    
    
    #fixing null date&value
  
    month_fixing = month_fixing[::-1]
    for m in range(len(month_fixing)):
        if m >= len(SO2_day):
            if SO2_day[-1] != month_fixing[-1]:
                lost_SO2 = m
                for i in time_line:
                    SO2_pos.insert(lost_SO2 , file_stat['測站'][0])
                    SO2_day.insert(lost_SO2 ,month_fixing[m])
                    SO2_stat.insert(lost_SO2 ,np.nan)
            
        if SO2_day[m] != month_fixing[m]:
            lost_SO2 = m
            
        if month_fixing[m] in SO2_day:
            pass
        else:
            
            for i in time_line:
                SO2_pos.insert(lost_SO2 , file_stat['測站'][0])
                SO2_day.insert(lost_SO2 ,month_fixing[m])
                SO2_stat.insert(lost_SO2 ,np.nan)
                
        
        
    for m in range(len(month_fixing)):
        if m >= len(NO2_day):
            if NO2_day[-1] != month_fixing[-1]:
                lost_NO2 = m
                for i in time_line:
                    NO2_pos.insert(lost_NO2, file_stat['測站'][0])
                    NO2_day.insert(lost_NO2, month_fixing[m])
                    NO2_stat.insert(lost_NO2, np.nan)
            
        if NO2_day[m] != month_fixing[m]:
            lost_NO2 = m
  
        if month_fixing[m] in NO2_day:
            pass
        else:
            for i in time_line:
                NO2_pos.insert(lost_NO2, file_stat['測站'][0])
                NO2_day.insert(lost_NO2, month_fixing[m])
                NO2_stat.insert(lost_NO2, np.nan)

        
    for m in range(len(month_fixing)):
        if m >= len(NO_day):
            if NO_day[-1] != month_fixing[-1]:
                lost_NO = m
                for i in time_line:
                    NO_pos.insert(lost_NO , file_stat['測站'][0])
                    NO_day.insert(lost_NO ,month_fixing[m])
                    NO_stat.insert(lost_NO ,np.nan)
            
        if NO_day[m] != month_fixing[m]:
            lost_NO = m
           
        if month_fixing[m] in NO_day:
            pass
        else:
            for i in time_line:
                NO_pos.insert(lost_NO , file_stat['測站'][0])
                NO_day.insert(lost_NO ,month_fixing[m])
                NO_stat.insert(lost_NO ,np.nan)
            


    for m in range(len(month_fixing)):
        if m >= len(NOX_day):
            if NOX_day[-1] != month_fixing[-1]:
                lost_NOX = m
                for i in time_line:
                    NOX_pos.insert(lost_NOX , file_stat['測站'][0])
                    NOX_day.insert(lost_NOX ,month_fixing[m])
                    NOX_stat.insert(lost_NOX ,np.nan)
            
        if NOX_day[m] != month_fixing[m]:
            lost_NOX = m

        if month_fixing[m] in NOX_day:
            pass
        else:
            for i in time_line:
                NOX_pos.insert(lost_NOX , file_stat['測站'][0])
                NOX_day.insert(lost_NOX ,month_fixing[m])
                NOX_stat.insert(lost_NOX ,np.nan)
           


    for m in range(len(month_fixing)):
        if m >= len(O3_day):
            if O3_day[-1] != month_fixing[-1]:
                lost_O3 = m
                for i in time_line:
                    O3_pos.insert(lost_O3 , file_stat['測站'][0])
                    O3_day.insert(lost_O3 ,month_fixing[m])
                    O3_stat.insert(lost_O3 ,np.nan)
            
        if O3_day[m] != month_fixing[m]:
            lost_O3 = m
            
        if month_fixing[m] in O3_day:
            pass
        else:
            for i in time_line:
                O3_pos.insert(lost_O3 , file_stat['測站'][0])
                O3_day.insert(lost_O3 ,month_fixing[m])
                O3_stat.insert(lost_O3 ,np.nan)
           
      
    for m in range(len(month_fixing)):
        if m >= len(PM10_day):
            if PM10_day[-1] != month_fixing[-1]:
                lost_PM10 = m
                for i in time_line:
                    PM10_pos.insert(lost_PM10 , file_stat['測站'][0])
                    PM10_day.insert(lost_PM10 , month_fixing[m])
                    PM10_stat.insert(lost_PM10 ,np.nan)
            
        if PM10_day[m] != month_fixing[m]:
            lost_PM10 = m
            
        if month_fixing[m] in PM10_day:
            pass
        else:
            for i in time_line:
                PM10_pos.insert(lost_PM10 , file_stat['測站'][0])
                PM10_day.insert(lost_PM10 , month_fixing[m])
                PM10_stat.insert(lost_PM10 ,np.nan)
           

    for m in range(len(month_fixing)):
        if m >= len(PM25_day):
            if PM25_day[-1] != month_fixing[-1]:
                lost_PM25 = m
                for i in time_line:
                    PM25_pos.insert(lost_PM25 , file_stat['測站'][0])
                    PM25_day.insert(lost_PM25 , month_fixing[m])
                    PM25_stat.insert(lost_PM25 ,np.nan)
            
        if PM25_day[m] != month_fixing[m]:
            lost_PM25 = m
        
        if month_fixing[m] in PM25_day:
            pass
        else:
            for i in time_line:
                PM25_pos.insert(lost_PM25 , file_stat['測站'][0])
                PM25_day.insert(lost_PM25 , month_fixing[m])
                PM25_stat.insert(lost_PM25 ,np.nan)
         
    
    
    #for m in range(len(month_fixing)):
    #    if m >= len(NMHC_day):
    #        if NMHC_day[-1] != month_fixing[-1]:
    #            lost_NMHC = m
    #            for i in time_line:
    #                NMHC_pos.insert(lost_NMHC, file_stat['測站'][0])
    #                NMHC_day.insert(lost_NMHC, month_fixing[m])
    #                NMHC_stat.insert(lost_NMHC, np.nan)
    #        
    #    if NMHC_day[m] != month_fixing[m]:
    #       lost_NMHC = m
    #    
    #    if month_fixing[m] in NMHC_day:
    #        pass
    #    else:
    #        for i in time_line:
    #            NMHC_pos.insert(lost_NMHC, file_stat['測站'][0])
    #            NMHC_day.insert(lost_NMHC, month_fixing[m])
    #            NMHC_stat.insert(lost_NMHC, np.nan)
           


    # Correction 
    SO2_stat = np.array(SO2_stat)
    NO2_stat = np.array(NO2_stat)
    NO_stat = np.array(NO_stat)
    NOX_stat = np.array(NOX_stat)
    O3_stat = np.array(O3_stat)
    PM10_stat = np.array(PM10_stat)
    PM25_stat = np.array(PM25_stat)
    #NMHC_stat = np.array(NMHC_stat)
    
    SO2_stat = SO2_stat.reshape(int(len(SO2_stat)/len(time_line)),len(time_line))
    NO2_stat = NO2_stat.reshape(int(len(NO2_stat)/len(time_line)),len(time_line))
    NO_stat = NO_stat.reshape(int(len(NO_stat)/len(time_line)),len(time_line))
    NOX_stat = NOX_stat.reshape(int(len(NOX_stat)/len(time_line)),len(time_line))
    O3_stat = O3_stat.reshape(int(len(O3_stat)/len(time_line)),len(time_line))
    PM10_stat = PM10_stat.reshape(int(len(PM10_stat)/len(time_line)),len(time_line))
    PM25_stat = PM25_stat.reshape(int(len(PM25_stat)/len(time_line)),len(time_line))
    #NMHC_stat = NMHC_stat.reshape(int(len(NMHC_stat)/len(time_line)),len(time_line))
    
    SO2_stat = SO2_stat[::-1, :]
    SO2_stat = SO2_stat.flatten()
    NO2_stat = NO2_stat[::-1, :]
    NO2_stat = NO2_stat.flatten()
    NO_stat = NO_stat[::-1, :]
    NO_stat = NO_stat.flatten()
    NOX_stat = NOX_stat[::-1, :]
    NOX_stat = NOX_stat.flatten()
    O3_stat = O3_stat[::-1, :]
    O3_stat = O3_stat.flatten()
    PM10_stat = PM10_stat[::-1, :]
    PM10_stat = PM10_stat.flatten()
    PM25_stat = PM25_stat[::-1, :]
    PM25_stat = PM25_stat.flatten()
    #NMHC_stat = NMHC_stat[::-1, :]
    #NMHC_stat = NMHC_stat.flatten()
    
    


    diff_lon = []
    diff_lat = []
    true_lon = []
    true_lat = []
    array_lon = []
    array_lat = []
    s = 0
    dataset_geo = Dataset(nc_geo)
    LON = dataset_geo.variables['LON'][0, 0, :, :]
    LAT = dataset_geo.variables['LAT'][0, 0, :, :]
    for j in range(np.size(LON, axis=0)):
        for i in range(np.size(LON, axis=1)):
            dis_lon = abs(LON[j, i]-stat_lon[stat_code])
            dis_lat = abs(LAT[j, i]-stat_lat[stat_code])
            if dis_lon<=(3/107.779) and dis_lat<=(3/111.321):
                print(LON[j, i]," ", LAT[j, i], file_csv['測站名稱'][stat_code],"位置偵測成功!")
                array_lon.append(0)
                array_lat.append(0)
                diff_lon.append(0)
                diff_lat.append(0)
                true_lon.append(0)
                true_lat.append(0)
                array_lon[s] = i
                array_lat[s] = j
                diff_lon[s] = dis_lon
                diff_lat[s] = dis_lat
                true_lon[s] = LON[j, i]
                true_lat[s] = LAT[j, i]
                s = s + 1 
                x = diff_lon.index(min(diff_lon))
                y = diff_lat.index(min(diff_lat))
                t_lon = true_lon[x]
                t_lat = true_lat[y]
                a_lon = array_lon[x]
                a_lat = array_lat[y]

    print("精確定位點: ", t_lon, t_lat )
    print("陣列位置: ", a_lon, a_lat)

    #i = col 經度
    #j = row 緯度


    dataset_CONC = Dataset(nc_file)
    SO2 = dataset_CONC.variables['SO2']
    NO2 = dataset_CONC.variables['NO2']
    NO = dataset_CONC.variables['NO']
    NOX = dataset_CONC.variables['NOX']
    O3 = dataset_CONC.variables['O3']
    PM25_TOT = dataset_CONC.variables['PM25_TOT']
    PM10 = dataset_CONC.variables['PM10']

    #NMHC Calculation
    ETH = dataset_CONC.variables['ETH'][:, 0, :, :]
    TOL = dataset_CONC.variables['TOL'][:, 0, :, :]
    XYL = dataset_CONC.variables['XYL'][:, 0, :, :]
    NMHC = ETH * 2 + TOL * 7 + XYL * 8.9




    #PLOT
    fig = plt.figure(figsize=(10, 17))
    
    SO2 = SO2[:, 0, a_lat, a_lon]
    SO2 = SO2[71:71+len(SO2)]
    x_space = np.arange(0, len(SO2), 1) 
    x_space_plus = np.arange(0, len(SO2_stat), 1)
    #print(SO2)
    ax = fig.add_subplot(8, 1, 1)
    #ax.axes.xaxis.set_visible(False)
    ax.axes.xaxis.set_ticklabels([])
    ax.grid(linestyle='--', alpha=0.57, zorder=2)
    ax.plot(x_space, SO2, color='blue', label='Sim')
    ax.scatter(x_space_plus, SO2_stat, s=4.5, color='red', label='Obs')
    ax.legend()
    

    NO2 = NO2[:, 0, a_lat, a_lon]
    NO2 = NO2[71:71+len(NO2)]
    
    x_space = np.arange(0, len(NO2), 1) 
    x_space_plus = np.arange(0, len(NO2_stat), 1)
    #print(SO2)
    ax = fig.add_subplot(8, 1, 2)
    #ax.axes.xaxis.set_visible(False)
    ax.axes.xaxis.set_ticklabels([])
    ax.grid(linestyle='--', alpha=0.57, zorder=2)
    ax.plot(x_space, NO2, color='blue', label='Sim')
    ax.scatter(x_space_plus, NO2_stat, s=4.5, color='red', label='Obs')
    

    NO = NO[:, 0, a_lat, a_lon]
    NO = NO[71:71+len(NO)]
    NO_T = NO + NO2
    NO_T_stat = []
    NO_T_stat = NO_stat + NO2_stat
    x_space = np.arange(0, len(NO), 1)
    x_space_plus = np.arange(0, len(NO_T_stat), 1)
    #print(SO2)
    ax = fig.add_subplot(8, 1, 3)
    #ax.axes.xaxis.set_visible(False)
    ax.axes.xaxis.set_ticklabels([])
    ax.grid(linestyle='--', alpha=0.57, zorder=2)
    ax.plot(x_space, NO_T, color='blue', label='Sim')
    ax.scatter(x_space_plus, NO_T_stat, s=4.5, color='red', label='Obs')

    

    NOX = NOX[:, 0, a_lat, a_lon]
    NOX = NOX[71:71+len(NOX)]
  
    x_space = np.arange(0, len(NOX), 1)
    x_space_plus = np.arange(0, len(NOX_stat), 1) 
    #print(SO2)
    ax = fig.add_subplot(8, 1, 4)
    #ax.axes.xaxis.set_visible(False)
    ax.axes.xaxis.set_ticklabels([])
    ax.grid(linestyle='--', alpha=0.57, zorder=2)
    ax.plot(x_space, NOX, color='blue', label='Sim')
    ax.scatter(x_space_plus, NOX_stat, s=4.5, color='red', label='Obs')

    
    
    O3 = O3[:, 0, a_lat, a_lon]
    O3 = O3[71:71+len(O3)]
   
    x_space = np.arange(0, len(O3), 1)
    x_space_plus = np.arange(0, len(O3_stat), 1) 
    #print(SO2)
    ax = fig.add_subplot(8, 1, 5)
    #ax.axes.xaxis.set_visible(False)
    ax.axes.xaxis.set_ticklabels([])
    ax.grid(linestyle='--', alpha=0.57, zorder=2)
    ax.plot(x_space, O3, color='blue', label='Sim')
    ax.scatter(x_space_plus, O3_stat, s=4.5, color='red', label='Obs')



    PM10 = PM10[:, 0, a_lat, a_lon]
    PM10 = PM10[71:71+len(PM10)]
    
    x_space = np.arange(0, len(PM10), 1)
    x_space_plus = np.arange(0, len(PM10_stat), 1) 
    #print(SO2)
    ax = fig.add_subplot(8, 1, 6)
    #ax.axes.xaxis.set_visible(False)
    ax.axes.xaxis.set_ticklabels([])
    ax.grid(linestyle='--', alpha=0.57, zorder=2)
    ax.plot(x_space, PM10, color='blue', label='Sim')
    ax.scatter(x_space_plus, PM10_stat, s=4.5, color='red', label='Obs')

    
    
    PM25_TOT = PM25_TOT[:, 0, a_lat, a_lon]
    PM25_TOT = PM25_TOT[71:71+len(PM25_TOT)]
   
    x_space = np.arange(0, len(PM25_TOT), 1) 
    x_space_plus = np.arange(0, len(PM25_stat), 1) 
    #print(SO2)
    ax = fig.add_subplot(8, 1, 7)
    #ax.axes.xaxis.set_visible(False)
    ax.axes.xaxis.set_ticklabels([])
    ax.grid(linestyle='--', alpha=0.57, zorder=2)
    ax.plot(x_space, PM25_TOT, color='blue', label='Sim')
    ax.scatter(x_space_plus, PM25_stat, s=4.5, color='red', label='Obs')



    NMHC = NMHC[:, a_lat, a_lon]
    NMHC = NMHC[71:71+len(NMHC)]
   
    x_space = np.arange(0, len(NMHC), 1) 
    x_space_plus = np.arange(0, len(NMHC_stat), 1) 
    #print(SO2)
    ax = fig.add_subplot(8, 1, 8)
    #ax.axes.xaxis.set_visible(False)
    ax.axes.xaxis.set_ticklabels([])
    ax.grid(linestyle='--', alpha=0.57, zorder=2)
    ax.plot(x_space, NMHC, color='blue', label='Sim')
    ax.scatter(x_space_plus, NMHC_stat, s=4.5, color='red', label='Obs')

    #domain_SO2
    month_fixing = month_fixing[::-1]
    dataframe = pd.DataFrame({'日期':month_fixing, '測站':SO2_pos, 'SO2測站值':SO2_stat
    ,'NO2測站值':NO2_stat
    ,'NO+NO2測站值':NO_T_stat
    ,'NOX測站值':NOX_stat
    ,'O3測站值':O3_stat
    ,'PM10測站值':PM10_stat
    ,'PM2.5測站值':PM25_stat
 
    ,'SO2模擬值': SO2
    ,'NO2模擬值':NO2
    ,'NO+NO2模擬值':NO_T
    ,'NOX模擬值':NOX
    ,'O3模擬值':O3
    ,'PM10模擬值':PM10
    ,'PM2.5模擬值':PM25_TOT})
    #,'NMHC模擬值':NMHC})
    dataframe.to_csv(file_csv['測站名稱'][stat_code]+month[f]+"觀測與模擬值.csv", index=False, sep=',', encoding='big5')
   
    
    
    plt.tight_layout()
    plt.show()


    #NMHC = data_nc.variables['NMHC']
    #print(file_csv)

    #print(file_csv['測站名稱'][:])
