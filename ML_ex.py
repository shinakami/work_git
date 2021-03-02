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
#from matplotlib.mlab import griddata
import scipy as sp
from scipy.stats import gaussian_kde
from scipy import interpolate
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy.linalg as la
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import csv
from sklearn.cluster import KMeans
#average linkage


X = [[i] for i in [0, 1.414, 2.000, 4.472, 5.657, 6.708, 5.099, 7.280]]
Z = linkage(X, 'average')
fig = plt.figure(figsize=(9, 9))
dn = dendrogram(Z)

plt.title("Average linkage", fontsize=20)
plt.ylabel("Distance", fontsize=18)
#plt.show()


A = [(1,0,0,1,0,0,0,0,0),(1,0,1,0,0,0,0,0,0),(1,1,0,0,0,0,0,0,0),(0,1,1,0,1,0,0,0,0),(0,1,1,2,0,0,0,0,0),(0,1,0,0,1,0,0,0,0),(0,1,0,0,1,0,0,0,0),
        (0,0,1,1,0,0,0,0,0),(0,1,0,0,0,0,0,0,1),(0,0,0,0,0,1,1,1,0),(0,0,0,0,0,0,1,1,1),(0,0,0,0,0,0,0,1,1)]

k=2
U, s, V = la.svd(A)
Uk = U[:, 0:k]
Sk = np.diag(s[0:k])
Vk = V[0:k, :]
set_US = Uk.dot(Sk)
new_A = set_US.dot(Vk)
fig = plt.figure(figsize=(9, 9))
plt.scatter(Uk[:,0], Uk[:,1], s=50)
plt.xlabel("SVD1", fontsize=18)
plt.ylabel("SVD2", fontsize=18)
#plt.show()
#print("Uk:")
#print(Uk)
#print("Sk:")
#print(Sk)
#print("Vk:")
#print(Vk)


#print("New_A_maxtrix:")
#print(new_A)

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/USArrests.csv')

Murder = df["Murder"]
Assault = df["Assault"]
UrbanPop= df["UrbanPop"]
Rape = df["Rape"]
#print(df)
dis = df.iloc[:,[0, 1, 2, 3]].values
#print(dis)

X_P = [(0,1,0,1,1,1),(2,0,4,0,0,1),(3,1,9,3,1,1)]
Y = [(4),(1),(6)]
X_p = np.linalg.pinv(X_P)
W = X_p.dot(Y)


dis = preprocessing.scale(dis)

T = linkage(dis, 'complete')
fig = plt.figure(figsize=(9, 9))
dendrogram = sch.dendrogram(sch.linkage(dis, method='complete'))

plt.title("Complete linkage(after scaling)", fontsize=20)
plt.ylabel("Distance", fontsize=18)
#plt.show()
fig = plt.figure(figsize=(9, 9))
model = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='complete')
model.fit(dis)
labels = model.labels_
plt.scatter(dis[labels==0, 0], dis[labels==0, 1], s=50, marker='o', color='red')
plt.scatter(dis[labels==1, 0], dis[labels==1, 1], s=50, marker='o', color='blue')
plt.scatter(dis[labels==2, 0], dis[labels==2, 1], s=50, marker='o', color='green')
plt.title("Complete linkage Clustering(after scaling)", fontsize=20)
#plt.show()

D, cla = make_classification(n_samples=60, n_classes=3, n_features=50,  n_informative=3)

print(D)
y = cla

pca = PCA(n_components=2)

D_new = pca.fit(D).transform(D)
#print(pca.components_)
for c, i in zip('rgb', [0, 1, 2]): 
    plt.scatter(D_new[y==i, 0], D_new[y==i, 1], c=c)

plt.xlabel("PCA1", fontsize=18)
plt.ylabel("PCA2", fontsize=18)
plt.title("60 observations", fontsize=20)
plt.show()
fig = plt.figure(figsize=(9, 9))
kmeans = KMeans(n_clusters=3)
kmeans.fit(D)

plt.scatter(D[:,0], D[:,1], c=kmeans.labels_, cmap='brg')
plt.title("K=3", fontsize=20)
plt.show()


fig = plt.figure(figsize=(9, 9))
kmeans = KMeans(n_clusters=2)
kmeans.fit(D)

plt.scatter(D[:,0], D[:,1], c=kmeans.labels_, cmap='brg')
plt.title("K=2", fontsize=20)
plt.show()

fig = plt.figure(figsize=(9, 9))
kmeans = KMeans(n_clusters=4)
kmeans.fit(D)
plt.scatter(D[:,0], D[:,1], c=kmeans.labels_, cmap='brg')
plt.title("K=4", fontsize=20)
plt.show()


fig = plt.figure(figsize=(9, 9))
kmeans = KMeans(n_clusters=3)
kmeans.fit(D_new)
plt.scatter(D_new[:,0], D_new[:,1], c=kmeans.labels_, cmap='brg')
plt.title("K=3(PCA1 & PCA2)", fontsize=20)
plt.show()


D = preprocessing.scale(D)
fig = plt.figure(figsize=(9, 9))
kmeans = KMeans(n_clusters=3)
kmeans.fit(D)

plt.scatter(D[:,0], D[:,1], c=kmeans.labels_, cmap='brg')
plt.title("K=3(after scaling)", fontsize=20)
plt.show()