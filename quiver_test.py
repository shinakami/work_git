
import numpy as np
import random as rd
import shapefile as shp
import imageio
import scipy as sp
from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt
from scipy import interpolate
X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)
fig, ax = plt.subplots()
ax.quiver(X, Y, U, V)
plt.show()

#load shapefile
sf = shp.Reader('taiwan_district.shp', encoding='ISO-8859-15')

initial_day = 1
all_day = 30
img_path = ['']
dc = np.arange(1, 11, 0.33)
for time in range(all_day):
    plt.figure(figsize = (6.4, 7))
    true_time = initial_day + time
    true_time = str(true_time)
    plt.title('2020-09-' + true_time + ' Xi winne the poor ',fontproperties = 'Times New Roman', fontsize = 15)

    for shape in sf.shapeRecords():
        
        # end index of each components of map
        l = shape.shape.parts
        
        len_l = len(l)  # how many parts of countries i.e. land and islands
        x = [i[0] for i in shape.shape.points[:]] # list of latitude
        y = [i[1] for i in shape.shape.points[:]] # list of longitude
        l.append(len(x)) # ensure the closure of the last component
        for k in range(len_l):
            # draw each component of map.
            # l[k] to l[k + 1] is the range of points that make this component
            plt.plot(x[l[k]:l[k + 1]],y[l[k]:l[k + 1]], 'k-')


    # display
    y_v = np.arange(21.7, 25.6, 0.1)
    #y_v_xi:source of pollution (y_axis)
    y_v_xi = np.linspace(25.5, 23, 20)
    y_v_xi = np.arange(25, 26, 0.05)
    #y_v_xi:source of pollution (y_axis)
    x_v_xi = np.linspace(120.5, 122.5, 20)

    x_v = np.arange(119, 123, 0.1)
    #con = np.linspace(20-dc[time] * 0.3, 10+dc[time] * 0.55, 20)
    U, V = np.meshgrid(x_v, y_v)
    u = 10 * U * dc[time]
    if time < 5:
        v = 20.8 * V  / dc[time] * 10
    con = np.linspace(20 - np.average(v.flatten())*0.001, 10 + np.average(u.flatten())*0.001, 20)
    #setting positions for interpolation
    spline = sp.interpolate.Rbf(x_v_xi, y_v_xi, con, epsilon = 2.8, function='gaussian')
    #contourF_boundary
    X, Y = np.meshgrid(x_v, y_v)
    con_data = spline(X, Y)
    
    plt.contourf(X, Y, con_data, 20, cmap=plt.cm.rainbow, vmax=abs(con_data).max(), vmin=abs(con_data).min())
    plt.clim(1, 20)
    cbar = plt.colorbar()
    cbar.set_label("Xi Fart (ppb)", fontsize=15)
    plt.quiver(x_v, y_v, u, v)
    plt.savefig('2020-09-' + true_time + '.png', dpi = 300)
    img_path[time] = '2020-09-' + true_time + '.png'
    if time < (all_day-1):
        img_path.append('')
    print(img_path[time])
    #plt.show()

gif_images = []
for path in img_path:
    gif_images.append(imageio.imread(path))
imageio.mimsave("test2.gif",gif_images,fps=5)

