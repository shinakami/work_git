import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import random as rd
from random import sample
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold
from scipy import interpolate
#(b)
print("excercise(b)")
def linear_model(x):
    Gaussian=np.random.normal(0,1, 40)
    for i in np.arange(0, len(Gaussian)):
        if(Gaussian[i]>=0):
            eps=Gaussian[i]
    y=2*x+eps
    return y

x=np.linspace(-3, 3, 20)
np.random.shuffle(x)
y=linear_model(x)
training_data=x[0:14]
testing_data=x[15:19]
fig, ax =plt.subplots(2,1)
block_for_tr=np.ndarray([3,3])
degree=[5,10,14]
for i in np.arange(0, len(degree)):
    block_for_tr[i][0]=degree[i]
#function_degree=5
s=(len(training_data),6)
X_matrix=np.zeros(s)
for d in np.arange(0, 6):
    for i in np.arange(0, len(training_data)):
        X_matrix[i][d]=x[i]**(5-d)
        

X_matrix_T=X_matrix.transpose()
X_inverse=np.linalg.inv(X_matrix_T.dot(X_matrix))
X_total=X_inverse.dot(X_matrix_T)
Wlin=X_total.dot(y[0:14])

#Formula after Regression
y_regress=Wlin[0]*(x[0:14]**5)+Wlin[1]*(x[0:14]**4)+Wlin[2]*(x[0:14]**3)+Wlin[3]*(x[0:14]**2)+Wlin[4]*(x[0:14]**1)+Wlin[5]*(x[0:14]**0)

#training error
y_regress_training=Wlin[0]*(x[0:14]**5)+Wlin[1]*(x[0:14]**4)+Wlin[2]*(x[0:14]**3)+Wlin[3]*(x[0:14]**2)+Wlin[4]*(x[0:14]**1)+Wlin[5]*(x[0:14]**0)
training_error=str(mean_squared_error(y[0:14], y_regress_training))


#testing error
y_regress_test=Wlin[0]*(x[15:19]**5)+Wlin[1]*(x[15:19]**4)+Wlin[2]*(x[15:19]**3)+Wlin[3]*(x[15:19]**2)+Wlin[4]*(x[15:19]**1)+Wlin[5]*(x[15:19]**0)
testing_error=str(mean_squared_error(y[15:19], y_regress_test))

ax[0].plot(x[0:14], y_regress[0:14], 's-', color="blue", label="traning model_degree=5", linewidth=5)
block_for_tr[0][1]=float(training_error)
block_for_tr[0][2]=float(testing_error)

#function_degree=10
s=(len(training_data),11)
X_matrix=np.zeros(s)
for d in np.arange(0, 11):
    for i in np.arange(0, len(training_data)):
        X_matrix[i][d]=x[i]**(10-d)
        

X_matrix_T=X_matrix.transpose()
X_inverse=np.linalg.inv(X_matrix_T.dot(X_matrix))
X_total=X_inverse.dot(X_matrix_T)
Wlin=X_total.dot(y[0:14])

#Formula after Regression
y_regress=Wlin[0]*(x[0:14]**10)+Wlin[1]*(x[0:14]**9)+Wlin[2]*(x[0:14]**8)+Wlin[3]*(x[0:14]**7)\
    +Wlin[4]*(x[0:14]**6)+Wlin[5]*(x[0:14]**5)+Wlin[6]*(x[0:14]**4)+Wlin[7]*(x[0:14]**3)\
        +Wlin[8]*(x[0:14]**2)+Wlin[9]*(x[0:14]**1)+Wlin[10]*(x[0:14]**0)

#training error
y_regress_training=Wlin[0]*(x[0:14]**10)+Wlin[1]*(x[0:14]**9)+Wlin[2]*(x[0:14]**8)+Wlin[3]*(x[0:14]**7)\
    +Wlin[4]*(x[0:14]**6)+Wlin[5]*(x[0:14]**5)+Wlin[6]*(x[0:14]**4)+Wlin[7]*(x[0:14]**3)\
        +Wlin[8]*(x[0:14]**2)+Wlin[9]*(x[0:14]**1)+Wlin[10]*(x[0:14]**0)
training_error=str(mean_squared_error(y[0:14], y_regress_training))


#testing error
y_regress_test=Wlin[0]*(x[15:19]**10)+Wlin[1]*(x[15:19]**9)+Wlin[2]*(x[15:19]**8)+Wlin[3]*(x[15:19]**7)\
    +Wlin[4]*(x[15:19]**6)+Wlin[5]*(x[15:19]**5)+Wlin[6]*(x[15:19]**4)+Wlin[7]*(x[15:19]**3)\
        +Wlin[8]*(x[15:19]**2)+Wlin[9]*(x[15:19]**1)+Wlin[10]*(x[15:19]**0)
testing_error=str(mean_squared_error(y[15:19], y_regress_test))

ax[0].plot(x[0:14], y_regress[0:14], 'o-', color="red", label="traning model_degree=10", linewidth=2.5)
block_for_tr[1][1]=float(training_error)
block_for_tr[1][2]=float(testing_error)

#function_degree=14
s=(len(training_data),15)
X_matrix=np.zeros(s)
for d in np.arange(0, 15):
    for i in np.arange(0, len(training_data)):
        X_matrix[i][d]=x[i]**(14-d)
        

X_matrix_T=X_matrix.transpose()
X_inverse=np.linalg.inv(X_matrix_T.dot(X_matrix))
X_total=X_inverse.dot(X_matrix_T)
Wlin=X_total.dot(y[0:14])

#Formula after Regression
y_regress=Wlin[0]*(x[0:14]**14)+Wlin[1]*(x[0:14]**13)+Wlin[2]*(x[0:14]**12)+Wlin[3]*(x[0:14]**11) \
    +Wlin[4]*(x[0:14]**10)+Wlin[5]*(x[0:14]**9)+Wlin[6]*(x[0:14]**8)+Wlin[7]*(x[0:14]**7)+Wlin[8]*(x[0:14]**6)\
        +Wlin[9]*(x[0:14]**5)+Wlin[10]*(x[0:14]**4)+Wlin[11]*(x[0:14]**3)+Wlin[12]*(x[0:14]**2)+Wlin[13]*(x[0:14]**1)+Wlin[14]*(x[0:14]**0)

#training error
y_regress_training=Wlin[0]*(x[0:14]**14)+Wlin[1]*(x[0:14]**13)+Wlin[2]*(x[0:14]**12)+Wlin[3]*(x[0:14]**11)\
    +Wlin[4]*(x[0:14]**10)+Wlin[5]*(x[0:14]**9)+Wlin[6]*(x[0:14]**8)+Wlin[7]*(x[0:14]**7)+Wlin[8]*(x[0:14]**6)\
        +Wlin[9]*(x[0:14]**5)+Wlin[10]*(x[0:14]**4)+Wlin[11]*(x[0:14]**3)+Wlin[12]*(x[0:14]**2)+Wlin[13]*(x[0:14]**1)+Wlin[14]*(x[0:14]**0)
training_error=str(mean_squared_error(y[0:14], y_regress_training))


#testing error
y_regress_test=Wlin[0]*(x[15:19]**14)+Wlin[1]*(x[15:19]**13)+Wlin[2]*(x[15:19]**12)+Wlin[3]*(x[15:19]**11)\
    +Wlin[4]*(x[15:19]**10)+Wlin[5]*(x[15:19]**9)+Wlin[6]*(x[15:19]**8)+Wlin[7]*(x[15:19]**7)+Wlin[8]*(x[15:19]**6)\
        +Wlin[9]*(x[15:19]**5)+Wlin[10]*(x[15:19]**4)+Wlin[11]*(x[15:19]**3)+Wlin[12]*(x[15:19]**2)+Wlin[13]*(x[15:19]**1)+Wlin[14]*(x[15:19]**0)
testing_error=str(mean_squared_error(y[15:19], y_regress_test))

block_for_tr[2][1]=float(training_error)
block_for_tr[2][2]=float(testing_error)

func=interpolate.interp1d(x[0:14], y_regress, kind="cubic")
x_new=np.linspace(x[0:14].min(), x[0:14].max(), 100)
func_y_regress=func(x_new)
ax[0].plot(x_new, func_y_regress, color="green", label="traning model_degree=14", linewidth=3)

ax[0].legend()
ax[0].set_ylim(y.min(), y.max())
ax[0].set_xlim(x.min(), x.max())


collabel=("degree", "training error", "testing error")
ax[1].axis("off")
ax[1].axis("tight")
ax[1].table(cellText=block_for_tr, colLabels=collabel, loc="best")





#-------------------------------------------------------------------------------------------------------




#Leave-one-out CV

#function_degree=5,10,14
block_for_LOO=np.ndarray([3,2])
degree=[5,10,14]
for i in np.arange(0, len(degree)):
    block_for_LOO[i][0]=degree[i]
for dg in np.arange(0, len(degree)):
    LOOCV_testError=np.zeros(20)
    if(dg==0):
        y_regress_LOOCV_0=np.zeros(20)
    elif(dg==1):
        y_regress_LOOCV_1=np.zeros(20)
    elif(dg==2):
        y_regress_LOOCV_2=np.zeros(20)
    for a in np.arange(0, len(x)):
        testing_data_LOOCV=x[a]
        training_data_LOOCV=np.delete(x, a)
        y_LOOCV=np.delete(y, a)
        s=(len(training_data_LOOCV),degree[dg]+1)
        X_matrix=np.zeros(s)
        for d in np.arange(0, degree[dg]+1):
            for i in np.arange(0, len(training_data_LOOCV)):
                X_matrix[i][d]=training_data_LOOCV[i]**(degree[dg]-d)

        X_matrix_T=X_matrix.transpose()
        X_inverse=np.linalg.inv(X_matrix_T.dot(X_matrix))
        X_total=X_inverse.dot(X_matrix_T)

        if(dg==0):
            Wlin_0=X_total.dot(y_LOOCV)
        elif(dg==1):
            Wlin_1=X_total.dot(y_LOOCV)
        elif(dg==2):
            Wlin_2=X_total.dot(y_LOOCV)

        training_data_LOOCV=np.insert(training_data_LOOCV, a, testing_data_LOOCV, axis=0)
        y_LOOCV=np.insert(y_LOOCV, a, y[a], axis=0)
        #LOOCV Model
        if(dg==0):
            y_regress_LOOCV_0[a]=Wlin_0[0]*(testing_data_LOOCV**5)+Wlin_0[1]*(testing_data_LOOCV**4)+Wlin_0[2]*(testing_data_LOOCV**3)\
                +Wlin_0[3]*(testing_data_LOOCV**2)+Wlin_0[4]*(testing_data_LOOCV**1)+Wlin_0[5]*(testing_data_LOOCV**0)
            LOOCV_testError[a]=(y_regress_LOOCV_0[a]-y_LOOCV[a])**2
        elif(dg==1):
            y_regress_LOOCV_1[a]=Wlin_1[0]*(testing_data_LOOCV**10)+Wlin_1[1]*(testing_data_LOOCV**9)+Wlin_1[2]*(testing_data_LOOCV**8)+Wlin_1[3]*(testing_data_LOOCV**7)\
                +Wlin_1[4]*(testing_data_LOOCV**6)+Wlin_1[5]*(testing_data_LOOCV**5)+Wlin_1[6]*(testing_data_LOOCV**4)+Wlin_1[7]*(testing_data_LOOCV**3)\
                    +Wlin_1[8]*(testing_data_LOOCV**2)+Wlin_1[9]*(testing_data_LOOCV**1)+Wlin_1[10]*(testing_data_LOOCV**0)
            LOOCV_testError[a]=(y_regress_LOOCV_1[a]-y_LOOCV[a])**2
        elif(dg==2):
            y_regress_LOOCV_2[a]=Wlin_2[0]*(testing_data_LOOCV**14)+Wlin_2[1]*(testing_data_LOOCV**13)+Wlin_2[2]*(testing_data_LOOCV**12)\
                +Wlin_2[3]*(testing_data_LOOCV**11)+Wlin_2[4]*(testing_data_LOOCV**10)+Wlin_2[5]*(testing_data_LOOCV**9)+Wlin_2[6]*(testing_data_LOOCV**8)\
                    +Wlin_2[7]*(testing_data_LOOCV**7)+Wlin_2[8]*(testing_data_LOOCV**6)+Wlin_2[9]*(testing_data_LOOCV**5)+Wlin_2[10]*(testing_data_LOOCV**4)\
                        +Wlin_2[11]*(testing_data_LOOCV**3)+Wlin_2[12]*(testing_data_LOOCV**2)\
                            +Wlin_2[13]*(testing_data_LOOCV**1)+Wlin_2[14]*(testing_data_LOOCV**0)
            LOOCV_testError[a]=(y_regress_LOOCV_2[a]-y_LOOCV[a])**2
        pass
        
        
    
    mean_squared_LOOCV=str(np.average(LOOCV_testError))
    block_for_LOO[dg][1]=float(mean_squared_LOOCV)
    

fig, ax =plt.subplots(2,1)

ax[0].plot(x, y_regress_LOOCV_0, color="blue", label="leave-one-out degree=5", linewidth=10)
ax[0].plot(x, y_regress_LOOCV_1, color="red", label="leave-one-out degree=10", linewidth=7)
ax[0].plot(x, y_regress_LOOCV_2, color="green", label="leave-one-out degree=14", linewidth=2.5)
ax[0].set_ylim(y.min(), y.max())
ax[0].set_xlim(x.min(), x.max())
ax[0].legend()

collabel=("degree", "leave-one-out error")
ax[1].axis("off")
ax[1].axis("tight")
ax[1].table(cellText=block_for_LOO, colLabels=collabel, loc="best")







#-------------------------------------------------------------------------------------------------------







#Five-Fold degree=5
fold=5
block_for_Five=np.ndarray([3,2])
fig, ax =plt.subplots(2,1)
#Five-Fold of n times
n=10
kf=KFold(n_splits=fold, shuffle=False)
Wlin_F=np.zeros((6,n*fold))
testing_Five_Fold_error=np.zeros((n, fold))
y_regress_Five_Fold=np.zeros(len(x))
a=0
for g in np.arange(0, n):
    a=0
    for train_index, test_index in kf.split(x):
        
        training_data_Fold=np.zeros(len(train_index))
        testing_data_Fold=np.zeros(len(test_index))
        y_Five_Fold=np.zeros(len(train_index))
        y_test=np.zeros(len(test_index))
        for i in np.arange(0, len(train_index)):
            training_data_Fold[i]=x[train_index[i]]
        for i in np.arange(0, len(test_index)):
            testing_data_Fold[i]=x[test_index[i]]
        for i in np.arange(0, len(train_index)):
            y_Five_Fold[i]=linear_model(x[train_index[i]])
        for i in np.arange(0, len(test_index)):
            y_test[i]=linear_model(x[test_index[i]])
        s=(len(train_index),6)
        X_matrix=np.zeros(s)
        for d in np.arange(0, 6):
            for i in np.arange(0, len(train_index)):
                X_matrix[i][d]=training_data_Fold[i]**(5-d)

        X_matrix_T=X_matrix.transpose()
        X_inverse=np.linalg.inv(X_matrix_T.dot(X_matrix))
        X_total=X_inverse.dot(X_matrix_T)
        #Five=Fold model
        Wlin=X_total.dot(y_Five_Fold)
        y_regress_Five_Fold=Wlin[0]*(testing_data_Fold**5)+Wlin[1]*(testing_data_Fold**4)+Wlin[2]*(testing_data_Fold**3)\
                +Wlin[3]*(testing_data_Fold**2)+Wlin[4]*(testing_data_Fold**1)+Wlin[5]*(testing_data_Fold**0)
        testing_Five_Fold_error[g][a]=mean_squared_error(y_test, y_regress_Five_Fold)
        #print(Wlin[0])
        for k in np.arange(0, 6):
            Wlin_F[k][a+fold*g]=Wlin[k]

        a=a+1
mean_squared_FiveFold=str(np.average(testing_Five_Fold_error.flatten()))

block_for_Five[0][1]=mean_squared_FiveFold
#average weighting of New Model
y_regress_Five_Fold=np.average(Wlin_F[0][:])*(x**5)+np.average(Wlin_F[1][:])*(x**4)+np.average(Wlin_F[2][:])*(x**3)\
                +np.average(Wlin_F[3][:])*(x**2)+np.average(Wlin_F[4][:])*(x**1)+np.average(Wlin_F[5][:])*(x**0)

func=interpolate.interp1d(x, y_regress_Five_Fold, kind="cubic")
x_new=np.linspace(x.min(), x.max(), 100)
func_y_regress_Five_5=func(x_new)
ax[0].plot(x_new,func_y_regress_Five_5, color="blue", label="Five-Fold degree=5", linewidth=1.5)




#Five-Fold degree=10
Wlin_F=np.zeros((11,n*fold))
testing_Five_Fold_error=np.zeros((n, fold))
y_regress_Five_Fold=np.zeros(len(x))
a=0
for g in np.arange(0, n):
    a=0
    for train_index, test_index in kf.split(x):
        
        training_data_Fold=np.zeros(len(train_index))
        testing_data_Fold=np.zeros(len(test_index))
        y_Five_Fold=np.zeros(len(train_index))
        y_test=np.zeros(len(test_index))
        for i in np.arange(0, len(train_index)):
            training_data_Fold[i]=x[train_index[i]]
        for i in np.arange(0, len(test_index)):
            testing_data_Fold[i]=x[test_index[i]]
        for i in np.arange(0, len(train_index)):
            y_Five_Fold[i]=linear_model(x[train_index[i]])
        for i in np.arange(0, len(test_index)):
            y_test[i]=linear_model(x[test_index[i]])
        s=(len(train_index),11)
        X_matrix=np.zeros(s)
        for d in np.arange(0, 11):
            for i in np.arange(0, len(train_index)):
                X_matrix[i][d]=training_data_Fold[i]**(10-d)

        X_matrix_T=X_matrix.transpose()
        X_inverse=np.linalg.inv(X_matrix_T.dot(X_matrix))
        X_total=X_inverse.dot(X_matrix_T)
        #Five=Fold model
        Wlin=X_total.dot(y_Five_Fold)
        y_regress_Five_Fold=Wlin[0]*(testing_data_Fold**10)+Wlin[1]*(testing_data_Fold**9)+Wlin[2]*(testing_data_Fold**8)\
                +Wlin[3]*(testing_data_Fold**7)+Wlin[4]*(testing_data_Fold**6)+Wlin[5]*(testing_data_Fold**5)+Wlin[6]*(testing_data_Fold**4)\
                    +Wlin[7]*(testing_data_Fold**3)+Wlin[8]*(testing_data_Fold**2)+Wlin[9]*(testing_data_Fold**1)+Wlin[10]*(testing_data_Fold**0)
        testing_Five_Fold_error[g][a]=mean_squared_error(y_test, y_regress_Five_Fold)
        #print(Wlin[0])
        for k in np.arange(0, 11):
            Wlin_F[k][a+fold*g]=Wlin[k]

        a=a+1
mean_squared_FiveFold=str(np.average(testing_Five_Fold_error.flatten()))

block_for_Five[1][1]=mean_squared_FiveFold
#average weighting of New Model
y_regress_Five_Fold=np.average(Wlin_F[0][:])*(x**10)+np.average(Wlin_F[1][:])*(x**9)+np.average(Wlin_F[2][:])*(x**8)\
                +np.average(Wlin_F[3][:])*(x**7)+np.average(Wlin_F[4][:])*(x**6)+np.average(Wlin_F[5][:])*(x**5)+np.average(Wlin_F[6][:])*(x**4)\
                    +np.average(Wlin_F[7][:])*(x**3)+np.average(Wlin_F[8][:])*(x**2)+np.average(Wlin_F[9][:])*(x**1)+np.average(Wlin_F[10][:])*(x**0)

func=interpolate.interp1d(x, y_regress_Five_Fold, kind="cubic")
x_new=np.linspace(x.min(), x.max(), 100)
func_y_regress_Five_5=func(x_new)
ax[0].plot(x_new,func_y_regress_Five_5, color="red", label="Five-Fold degree=10", linewidth=1.5)











#Five-Fold degree=14
Wlin_F=np.zeros((15,n*fold))
testing_Five_Fold_error=np.zeros((n, fold))
y_regress_Five_Fold=np.zeros(len(x))
a=0
for g in np.arange(0, n):
    a=0
    for train_index, test_index in kf.split(x):
        
        training_data_Fold=np.zeros(len(train_index))
        testing_data_Fold=np.zeros(len(test_index))
        y_Five_Fold=np.zeros(len(train_index))
        y_test=np.zeros(len(test_index))
        for i in np.arange(0, len(train_index)):
            training_data_Fold[i]=x[train_index[i]]
        for i in np.arange(0, len(test_index)):
            testing_data_Fold[i]=x[test_index[i]]
        for i in np.arange(0, len(train_index)):
            y_Five_Fold[i]=linear_model(x[train_index[i]])
        for i in np.arange(0, len(test_index)):
            y_test[i]=linear_model(x[test_index[i]])
        s=(len(train_index),15)
        X_matrix=np.zeros(s)
        for d in np.arange(0, 15):
            for i in np.arange(0, len(train_index)):
                X_matrix[i][d]=training_data_Fold[i]**(14-d)

        X_matrix_T=X_matrix.transpose()
        X_inverse=np.linalg.inv(X_matrix_T.dot(X_matrix))
        X_total=X_inverse.dot(X_matrix_T)
        #Five=Fold model
        Wlin=X_total.dot(y_Five_Fold)
        y_regress_Five_Fold=Wlin[0]*(testing_data_Fold**14)+Wlin[1]*(testing_data_Fold**13)+Wlin[2]*(testing_data_Fold**12)\
                +Wlin[3]*(testing_data_Fold**11)+Wlin[4]*(testing_data_Fold**10)+Wlin[5]*(testing_data_Fold**9)+Wlin[6]*(testing_data_Fold**8)\
                    +Wlin[7]*(testing_data_Fold**7)+Wlin[8]*(testing_data_Fold**6)+Wlin[9]*(testing_data_Fold**5)+Wlin[10]*(testing_data_Fold**4)\
                        +Wlin[11]*(testing_data_Fold**3)+Wlin[12]*(testing_data_Fold**2)+Wlin[13]*(testing_data_Fold**1)+Wlin[14]*(testing_data_Fold**0)
        testing_Five_Fold_error[g][a]=mean_squared_error(y_test, y_regress_Five_Fold)
        #print(Wlin[0])
        for k in np.arange(0, 15):
            Wlin_F[k][a+fold*g]=Wlin[k]

        a=a+1
mean_squared_FiveFold=str(np.average(testing_Five_Fold_error.flatten()))

block_for_Five[2][1]=mean_squared_FiveFold
#average weighting of New Model
y_regress_Five_Fold=np.average(Wlin_F[0][:])*(x**14)+np.average(Wlin_F[1][:])*(x**13)+np.average(Wlin_F[2][:])*(x**12)\
                +np.average(Wlin_F[3][:])*(x**11)+np.average(Wlin_F[4][:])*(x**10)+np.average(Wlin_F[5][:])*(x**9)+np.average(Wlin_F[6][:])*(x**8)\
                    +np.average(Wlin_F[7][:])*(x**7)+np.average(Wlin_F[8][:])*(x**6)+np.average(Wlin_F[9][:])*(x**5)+np.average(Wlin_F[10][:])*(x**4)\
                        +np.average(Wlin_F[11][:])*(x**3)+np.average(Wlin_F[12][:])*(x**2)+np.average(Wlin_F[13][:])*(x**1)+np.average(Wlin_F[14][:])*(x**0)

func=interpolate.interp1d(x, y_regress_Five_Fold, kind="cubic")
x_new=np.linspace(x.min(), x.max(), 100)
func_y_regress_Five_5=func(x_new)
ax[0].plot(x_new,func_y_regress_Five_5, color="green", label="Five-Fold degree=14", linewidth=1.5)

for i in np.arange(0, len(degree)):
    block_for_Five[i][0]=degree[i]

ax[0].set_ylim(y.min(), y.max())
ax[0].set_xlim(x.min(), x.max())
ax[0].legend()

collabel=("degree", "Five-Fold error")
ax[1].axis("off")
ax[1].axis("tight")
ax[1].table(cellText=block_for_Five, colLabels=collabel, loc="best")

plt.show()

