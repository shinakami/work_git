import cv2
import imageio
import numpy as np
import matplotlib.pyplot as plt
import os
from time import sleep
os.system('cls')
def get_images_from_video(video_name, time_F):
    video_images = []
    vc = cv2.VideoCapture(video_name)
    c = 1
    
    if vc.isOpened(): 
        rval, video_frame = vc.read()
    else:
        rval = False

    while rval:   
        rval, video_frame = vc.read()
        
        if(c % time_F == 0): 
            video_images.append(video_frame)     
        c = c + 1
    vc.release()
    
    return video_images

time_F = 1
video_name = 'holo.mp4' 
video_images = get_images_from_video(video_name, time_F) 
print("Start")



img_gif = []
#video_L = int(len(video_images) * 0.02)
video_L = 192
print(video_L)
for i in range(video_L):
    if i % 50 == 0:
        print('sleep')
        sleep(60)
    img_gif.append('')
    width = int(video_images[i].shape[1] * 0.15)
    height = int(video_images[i].shape[0] * 0.15)
    img_re = cv2.resize(video_images[i], (width, height), interpolation=cv2.INTER_CUBIC)
    img_re = img_re[:, :, [2, 1, 0]]
    fig = plt.figure(figsize=(10, 8))
    plt.title('HOLOchame!!', fontsize=20)
    plt.xlim(0, width)
    plt.ylim(height, 0)
    plt.xlabel('HOLO X')
    plt.ylabel('HOLO Y')
    for j in range(height):
        for k in range(width):

            plt.scatter(k, j, s=4, color=tuple(img_re[j, k, :]/255))
            

    plt.savefig('ochame'+str(i)+'.png', dpi=200)
    plt.close()
    os.system('cls')
    print('Finished', 'ochame'+str(i)+'.png')
    img_gif[i] = 'ochame'+str(i)+'.png'
gif_i = []
for p in img_gif:
    gif_i.append(imageio.imread(p))
imageio.mimsave("HOLOCHAME2.gif", gif_i, duration=0.001, fps=60)
print("OK!")


