import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import cv2
import math as ma
pio.templates.default = 'plotly_dark'
# Make figure with subplots
img_path = ['Uruha_Rushia_-_Portrait.png', 'Kiryu_Coco_-_Portrait.png']
OPPAI_label = ['Rushia OPPAI', 'Coco OPPAI']
t = 0
size_scale = [0.02, 1]
csize = [0.1, 1.6]
for im in img_path:
    fig = make_subplots(rows=1, cols=3, specs=[[{"type": "image"}, {"type": "scatter"}, {"type": "surface"}]])
    img = cv2.imread(im)
    img = img[:,:,[2,1,0]]

    x_b=np.arange(-9.5,9.5,0.25)
    y_b=np.arange(-9.5,9.5,0.25)
    x_b, y_b = np.meshgrid(x_b, y_b)

    z_b = size_scale[t]*np.exp(-((x_b-4)**2+(y_b-4)**2)**2/1000) + size_scale[t]*np.exp(-((x_b+4)**2+(y_b+4)**2)**2/1000) + 0.08*np.exp(-((x_b+4)**2+(y_b+4)**2)**2)+0.08*np.exp(-((x_b-4)**2+(y_b-4)**2)**2) 
    x_a = x_b.flatten()
    y_a = z_b.flatten()
   
    fig.add_trace(go.Image(z=img), row=1, col=1)
    fig.add_trace(go.Scatter(x=x_a, y=y_a, xaxis='x1', yaxis='y1', line_color='azure', mode='lines'), row=1, col=2)
    fig.add_trace(go.Surface(z=z_b, x=x_b, y=y_b, cmin=0, cmax=csize[t] ,colorscale='OrRd'), row=1, col=3)
    
    fig.update_xaxes(title_text='x', row=1, col=2)
    fig.update_yaxes(title_text='y', range=[0, 2], row=1, col=2)
    #fig = go.Figure(data=[go.Surface(z=z_b, x=x_b, y=y_b, cmin=0.2, cmax=0.7 ,colorscale='OrRd')])
    fig.update_layout(title=OPPAI_label[t], autosize=False,
                    width=1100, height=500,
                    margin=dict(l=65, r=50, b=65, t=90),  scene = dict(zaxis = dict(nticks=6, range=[0, 2])))
    

    fig.show(title=OPPAI_label[t])
    t = t + 1

fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter'}]])

x_line = np.linspace(4.8, 100, 1000)
y_line = np.log(x_line)/np.log(4.8)

x_line2 = np.linspace(5, 80, 800)
x_plus_v = np.linspace(80, 80, 100)
x_plus_v2 = np.linspace(80, 100, 100)
x_line2 = np.append(x_line2, x_plus_v)
x_line2 = np.append(x_line2, x_plus_v2)
y_line2 = np.zeros(1000)
for i in range(len(y_line2)):
    y_line2[i] = np.log(x_line2[i])/np.log(5)
    if x_line2[i] == 80:
        y_line2[i] = 2.721977 + 0.0015*(i-799)
    if x_line2[i] > 80:
        y_line2[i] = 3

fig.add_trace(go.Scatter(x=x_line, y=y_line, xaxis='x1', yaxis='y1', line_color='red', name='Trump', mode='lines'), row=1, col=1)
fig.add_trace(go.Scatter(x=x_line2, y=y_line2, xaxis='x1', yaxis='y1', line_color='blue', name='Biden', mode='lines'), row=1, col=1)
fig.update_layout(title='Biden-Trump 曲線', autosize=False,
                width=700, height=700,
                margin=dict(l=65, r=50, b=65, t=90)) 
fig.show()
