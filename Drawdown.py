import matplotlib.pyplot as plt

import matplotlib as mpl
import numpy as np
import time as ti
import pandas as pd

import random as rd
from matplotlib.font_manager import FontProperties
from matplotlib import cm
from matplotlib.ticker import MaxNLocator
from mpl_toolkits.mplot3d import Axes3D


import scipy as sp

from scipy import interpolate

font = 'Arial'

data = "Drawdown_point_radial.csv" #BH2
data_A = "Head_A2_Drawdown.csv" #BH3
data_B = "Head_B2_Drawdown.csv" #BH1
file_test = pd.read_csv(data)
file_test.columns = file_test.columns.str.strip()
x = file_test['X']
y = file_test['Y']

#如果是BH2(比較垂直井與輻射井的差異):z = abs(file_test['Drawdown_p']), z2 = abs(file_test['Drawdown_r'])
#如果是BH1跟BH1或是BH3: z = abs(file_test['Drawdown']), z2 = abs(file_test['Drawdown'])

z = abs(file_test['Drawdown_p'])
z2 = abs(file_test['Drawdown_r'])

fig = plt.figure(figsize = (9,9))
ax = fig.add_subplot(111, projection='3d')
spline = sp.interpolate.Rbf(x,y,z,function='cubic')
xi = np.linspace(min(x), max(x))
yi = np.linspace(min(y), max(y))
#zi = griddata(x, y, z, xi, yi, interp='linear')


X, Y = np.meshgrid(xi, yi)
Z = spline(X,Y)


plt.xlabel("Easting (m)", size=20, labelpad=15)
plt.ylabel("Northing (m)", size=20, labelpad=15)
ax.set_zlabel("Drawdown (m)", size=20, labelpad=15)
ax.set_zlim(0,40)
plt.title(" Normal well of BH2 ", fontproperties=font, size=25)
ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1, edgecolor='black')
#CS = plt.contourf(X, Y, Z, 15, cmap=plt.cm.rainbow, vmax=abs(Z).max(), vmin=-abs(Z).max())
#plt.colorbar()  # draw colorbar




fig = plt.figure(figsize = (9,9))
ax = fig.add_subplot(111, projection='3d')
spline2 = sp.interpolate.Rbf(x,y,z2,function='cubic')
Z2 = spline2(X,Y)
plt.xlabel("Easting (m)", size=20, labelpad=15)
plt.ylabel("Northing (m)", size=20, labelpad=15)
ax.set_zlabel("Drawdown (m)", size=20, labelpad=15)
ax.set_zlim(0,40)
plt.title("BH2", fontproperties=font, size=25)
ax.plot_wireframe(X, Y, Z2, rstride=1, cstride=1, edgecolor='black')
plt.show()

#2D Contour
plt.figure(figsize=(16,24))
plt.xlabel("Easting (m)", size=20)
plt.ylabel("Northing (m)", size=20)
plt.title("Normal well of BH2", fontproperties=font, size=25)
plt.xlim(xi.min(), xi.max())
plt.ylim(yi.min(), yi.max())
show_line=plt.contour(X, Y, Z, colors='k')
plt.clabel(show_line, inline=True, fontsize=15, fmt="%1.1f")
CS = plt.contourf(X, Y, Z, 20, cmap=plt.cm.rainbow, vmax=abs(Z).max(), vmin=abs(Z).min())

#plt.tight_layout()
plt.clim(0, 40)

cbar = plt.colorbar()
cbar.set_label("Drawdown (m))", fontsize=15)

plt.figure(figsize=(16,24))
plt.xlabel("Easting (m)", size=20)
plt.ylabel("Northing (m)", size=20)
plt.title("BH2", fontproperties=font, size=25)
plt.xlim(xi.min(), xi.max())
plt.ylim(yi.min(), yi.max())
show_line2=plt.contour(X, Y, Z2, colors='k')
plt.clabel(show_line2, inline=True, fontsize=15, fmt="%1.1f")
CS2 = plt.contourf(X, Y, Z2, 20, cmap=plt.cm.rainbow, vmax=abs(Z2).max(), vmin=abs(Z2).min())
#plt.tight_layout()
plt.clim(0, 40)
cbar = plt.colorbar()
cbar.set_label("Drawdown (m)", fontsize=15)
plt.show()