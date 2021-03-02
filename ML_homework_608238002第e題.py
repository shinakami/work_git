import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import random as rd
from random import sample
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold
from scipy import interpolate
#(d)
print("excercise(d)")
fig, ax =plt.subplots(2,1, figsize = (9,9))
color_test=['blue', 'lightblue', 'cyan']
color_LOO=['red', 'fuchsia', 'maroon']
color_Five=['green', 'lime', 'darkgreen']
m=20
data_lambda=[0.001/m, 1/m, 1000/m]
#unit maxtrix
I=np.eye(15)
block=np.zeros((3, 4))
for num in np.arange(0, len(data_lambda)):
    def linear_model(x):
        Gaussian=np.random.normal(0,1, m*2)
        for i in np.arange(0, len(Gaussian)):
            if(Gaussian[i]>=0):
                eps=Gaussian[i]
        y=2*x+eps
        return y

    x=np.arange(0, 1+1/(m-1), 1/(m-1))
    np.random.shuffle(x)
    y=linear_model(x)
    training_data=x[0:int(m*0.75-1)]
    testing_data=x[int(m*0.75):m-1]
    
    #function_degree=14
    s=(len(training_data),15)
    Z_matrix=np.zeros(s)
    for d in np.arange(0, 15):
        for i in np.arange(0, len(training_data)):
            Z_matrix[i][d]=x[i]**(14-d)
        
    #Regularization
    Z_matrix_T=Z_matrix.transpose()
    Z_inverse=np.linalg.inv(Z_matrix_T.dot(Z_matrix)+data_lambda[num]*I)
    Z_total=Z_inverse.dot(Z_matrix_T.dot(y[0:int(m*0.75-1)]))
    WReg=Z_total

    #Formula after Regression
    y_regress=WReg[0]*(x[0:int(m*0.75-1)]**14)+WReg[1]*(x[0:int(m*0.75-1)]**13)+WReg[2]*(x[0:int(m*0.75-1)]**12)+WReg[3]*(x[0:int(m*0.75-1)]**11) \
        +WReg[4]*(x[0:int(m*0.75-1)]**10)+WReg[5]*(x[0:int(m*0.75-1)]**9)+WReg[6]*(x[0:int(m*0.75-1)]**8)+WReg[7]*(x[0:int(m*0.75-1)]**7)+WReg[8]*(x[0:int(m*0.75-1)]**6)\
            +WReg[9]*(x[0:int(m*0.75-1)]**5)+WReg[10]*(x[0:int(m*0.75-1)]**4)+WReg[11]*(x[0:int(m*0.75-1)]**3)+WReg[12]*(x[0:int(m*0.75-1)]**2)+WReg[13]*(x[0:int(m*0.75-1)]**1)+WReg[14]*(x[0:int(m*0.75-1)]**0)

    #training error
    y_regress_training=WReg[0]*(x[0:int(m*0.75-1)]**14)+WReg[1]*(x[0:int(m*0.75-1)]**13)+WReg[2]*(x[0:int(m*0.75-1)]**12)+WReg[3]*(x[0:int(m*0.75-1)]**11) \
        +WReg[4]*(x[0:int(m*0.75-1)]**10)+WReg[5]*(x[0:int(m*0.75-1)]**9)+WReg[6]*(x[0:int(m*0.75-1)]**8)+WReg[7]*(x[0:int(m*0.75-1)]**7)+WReg[8]*(x[0:int(m*0.75-1)]**6)\
            +WReg[9]*(x[0:int(m*0.75-1)]**5)+WReg[10]*(x[0:int(m*0.75-1)]**4)+WReg[11]*(x[0:int(m*0.75-1)]**3)+WReg[12]*(x[0:int(m*0.75-1)]**2)+WReg[13]*(x[0:int(m*0.75-1)]**1)+WReg[14]*(x[0:int(m*0.75-1)]**0)
    training_error=str(mean_squared_error(y[0:int(m*0.75-1)], y_regress_training))


    #testing error
    y_regress_test=WReg[0]*(x[int(m*0.75):m-1]**14)+WReg[1]*(x[int(m*0.75):m-1]**13)+WReg[2]*(x[int(m*0.75):m-1]**12)+WReg[3]*(x[int(m*0.75):m-1]**11)\
        +WReg[4]*(x[int(m*0.75):m-1]**10)+WReg[5]*(x[int(m*0.75):m-1]**9)+WReg[6]*(x[int(m*0.75):m-1]**8)+WReg[7]*(x[int(m*0.75):m-1]**7)+WReg[8]*(x[int(m*0.75):m-1]**6)\
            +WReg[9]*(x[int(m*0.75):m-1]**5)+WReg[10]*(x[int(m*0.75):m-1]**4)+WReg[11]*(x[int(m*0.75):m-1]**3)+WReg[12]*(x[int(m*0.75):m-1]**2)+WReg[13]*(x[int(m*0.75):m-1]**1)+WReg[14]*(x[int(m*0.75):m-1]**0)
    testing_error=str(mean_squared_error(y[int(m*0.75):m-1], y_regress_test))




    func=interpolate.interp1d(x[0:int(m*0.75-1)], y_regress, kind="cubic")
    x_new=np.linspace(x[0:int(m*0.75-1)].min(), x[0:int(m*0.75-1)].max(), 100)
    func_y_regress=func(x_new)
    ax[0].plot(x_new, func_y_regress, color=color_test[num], label="traning model_lambda="+str(data_lambda[num]), linewidth=5)


    plt.ylim(y.min(), y.max())
    plt.xlim(x.min(), x.max())
    




    #-------------------------------------------------------------------------------------------------------




    #Leave-one-out CV

    #function_degree=14


    LOOCV_testError=np.zeros(m)
    y_regress_LOOCV_2=np.zeros(m)
    for a in np.arange(0, len(x)):
        testing_data_LOOCV=x[a]
        training_data_LOOCV=np.delete(x, a)
        y_LOOCV=np.delete(y, a)
        s=(len(training_data_LOOCV),15)
        Z_matrix=np.zeros(s)
        for d in np.arange(0, 15):
            for i in np.arange(0, len(training_data_LOOCV)):
                Z_matrix[i][d]=training_data_LOOCV[i]**(14-d)

        #Regularization
        Z_matrix_T=Z_matrix.transpose()
        Z_inverse=np.linalg.inv(Z_matrix_T.dot(Z_matrix)+data_lambda[num]*I)
        Z_total=Z_inverse.dot(Z_matrix_T.dot(y_LOOCV))
        WReg_2=Z_total
    

        training_data_LOOCV=np.insert(training_data_LOOCV, a, testing_data_LOOCV, axis=0)
        y_LOOCV=np.insert(y_LOOCV, a, y[a], axis=0)

        #LOOCV Model

        y_regress_LOOCV_2[a]=WReg_2[0]*(testing_data_LOOCV**14)+WReg_2[1]*(testing_data_LOOCV**13)+WReg_2[2]*(testing_data_LOOCV**12)\
            +WReg_2[3]*(testing_data_LOOCV**11)+WReg_2[4]*(testing_data_LOOCV**10)+WReg_2[5]*(testing_data_LOOCV**9)+WReg_2[6]*(testing_data_LOOCV**8)\
                +WReg_2[7]*(testing_data_LOOCV**7)+WReg_2[8]*(testing_data_LOOCV**6)+WReg_2[9]*(testing_data_LOOCV**5)+WReg_2[10]*(testing_data_LOOCV**4)\
                    +WReg_2[11]*(testing_data_LOOCV**3)+WReg_2[12]*(testing_data_LOOCV**2)\
                        +WReg_2[13]*(testing_data_LOOCV**1)+WReg_2[14]*(testing_data_LOOCV**0)
        LOOCV_testError[a]=(y_regress_LOOCV_2[a]-y_LOOCV[a])**2
               
    mean_squared_LOOCV=str(np.average(LOOCV_testError))
    func=interpolate.interp1d(x, y_regress_LOOCV_2, kind="cubic")
    x_new=np.linspace(x.min(), x.max(), 100)
    func_y_regress_LOOCV=func(x_new)

    ax[0].plot(x_new, func_y_regress_LOOCV, color=color_LOO[num], label="leave-one-out lambda="+str(data_lambda[num]), linewidth=2.5)
    plt.ylim(y.min(), y.max())
    plt.xlim(x.min(), x.max())









    #-------------------------------------------------------------------------------------------------------







    #Five-Fold degree=14
    fold=5
    #Five-Fold of n times
    n=10
    kf=KFold(n_splits=fold,shuffle=False)

    WReg_F=np.zeros((15,n*fold))
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
            Z_matrix=np.zeros(s)
            for d in np.arange(0, 15):
                for i in np.arange(0, len(train_index)):
                    Z_matrix[i][d]=training_data_Fold[i]**(14-d)
            
            #Regularization
            Z_matrix_T=Z_matrix.transpose()
            Z_inverse=np.linalg.inv(Z_matrix_T.dot(Z_matrix)+data_lambda[num]*I)
            Z_total=Z_inverse.dot(Z_matrix_T.dot(y_Five_Fold))
            WReg_five=Z_total

    
            #Five=Fold model
            y_regress_Five_Fold=WReg_five[0]*(testing_data_Fold**14)+WReg_five[1]*(testing_data_Fold**13)+WReg_five[2]*(testing_data_Fold**12)\
                    +WReg_five[3]*(testing_data_Fold**11)+WReg_five[4]*(testing_data_Fold**10)+WReg_five[5]*(testing_data_Fold**9)+WReg_five[6]*(testing_data_Fold**8)\
                        +WReg_five[7]*(testing_data_Fold**7)+WReg_five[8]*(testing_data_Fold**6)+WReg_five[9]*(testing_data_Fold**5)+WReg_five[10]*(testing_data_Fold**4)\
                            +WReg_five[11]*(testing_data_Fold**3)+WReg_five[12]*(testing_data_Fold**2)+WReg_five[13]*(testing_data_Fold**1)+WReg_five[14]*(testing_data_Fold**0)
            testing_Five_Fold_error[g][a]=mean_squared_error(y_test, y_regress_Five_Fold)
            #print(Wlin[0])
            for k in np.arange(0, 15):
                WReg_F[k][a+fold*g]=WReg_five[k]

            a=a+1
    mean_squared_FiveFold=str(np.average(testing_Five_Fold_error.flatten()))


    #average weighting of New Model
    y_regress_Five_Fold=np.average(WReg_F[0][:])*(x**14)+np.average(WReg_F[1][:])*(x**13)+np.average(WReg_F[2][:])*(x**12)\
                    +np.average(WReg_F[3][:])*(x**11)+np.average(WReg_F[4][:])*(x**10)+np.average(WReg_F[5][:])*(x**9)+np.average(WReg_F[6][:])*(x**8)\
                        +np.average(WReg_F[7][:])*(x**7)+np.average(WReg_F[8][:])*(x**6)+np.average(WReg_F[9][:])*(x**5)+np.average(WReg_F[10][:])*(x**4)\
                            +np.average(WReg_F[11][:])*(x**3)+np.average(WReg_F[12][:])*(x**2)+np.average(WReg_F[13][:])*(x**1)+np.average(WReg_F[14][:])*(x**0)

    func=interpolate.interp1d(x, y_regress_Five_Fold, kind="cubic")
    x_new=np.linspace(x.min(), x.max(), 100)
    func_y_regress_Five_5=func(x_new)
    ax[0].plot(x_new,func_y_regress_Five_5, color=color_Five[num], label="Five-Fold lambda="+str(data_lambda[num]), linewidth=1.5)


    #ax[0].set_ylim(y.min(), y.max())
    #ax[0].set_xlim(x.min(), x.max())
    print("lambda="+str(data_lambda[num]))
    block[num][3]=data_lambda[num]
    block[0][num]=testing_error
    print(block[0][num])
    block[1][num]=mean_squared_LOOCV
    print(block[1][num])
    block[2][num]=mean_squared_FiveFold
    print(block[2][num])
    collabel=("testing error", "Leave-one-out error", "Five-Fold error", "lambda")
    table=ax[1].table(cellText=block, colLabels=collabel, loc="center")
    table.set_fontsize(20)
    table.scale(1.2,1.2)
    ax[1].axis("off")
    ax[1].axis("tight")

    ax[0].legend()
    plt.tight_layout
    
plt.show()








































































plt.show()

