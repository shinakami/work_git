import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import random as rd
from random import sample
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold

#(a)
print("excercise(a)")
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

#y=ax+b
s=(len(training_data),2)
X_matrix=np.zeros(s)
for i in np.arange(0, len(training_data)):
    X_matrix[i][0]=x[i]
    X_matrix[i][1]=1

X_matrix_T=X_matrix.transpose()
X_inverse=np.linalg.inv(X_matrix_T.dot(X_matrix))
X_total=X_inverse.dot(X_matrix_T)
Wlin=X_total.dot(y[0:14])

#Formula after Regression
y_regress=Wlin[0]*x+Wlin[1]

#training error
y_regress_training=Wlin[0]*x[0:14]+Wlin[1]
training_error=str(mean_squared_error(y[0:14], y_regress_training))
print("training error: ", training_error)

#testing error
y_regress_test=Wlin[0]*x[15:19]+Wlin[1]
testing_error=str(mean_squared_error(y[15:19], y_regress_test))
print("testing error: ", testing_error)







#-------------------------------------------------------------------------------------------------------







#Leave-one-out CV
LOOCV_testError=np.zeros(20)
y_regress_LOOCV=np.zeros(20)
for a in np.arange(0, len(x)):
    testing_data_LOOCV=x[a]
    training_data_LOOCV=np.delete(x, a)
    y_LOOCV=np.delete(y, a)
    s=(len(training_data_LOOCV),2)
    X_matrix=np.zeros(s)
    for i in np.arange(0, len(training_data_LOOCV)):
        X_matrix[i][0]=training_data_LOOCV[i]
        X_matrix[i][1]=1

    X_matrix_T=X_matrix.transpose()
    X_inverse=np.linalg.inv(X_matrix_T.dot(X_matrix))
    X_total=X_inverse.dot(X_matrix_T)
    #LOOCV Model
    Wlin=X_total.dot(y_LOOCV)
    training_data_LOOCV=np.insert(training_data_LOOCV, a, testing_data_LOOCV, axis=0)
    y_LOOCV=np.insert(y_LOOCV, a, y[a], axis=0)
    y_regress_LOOCV[a]=Wlin[0]*testing_data_LOOCV+Wlin[1]
    LOOCV_testError[a]=(y_regress_LOOCV[a]-y_LOOCV[a])**2

mean_squared_LOOCV=str(np.average(LOOCV_testError))

print("leave-one-out: ", mean_squared_LOOCV)









#-------------------------------------------------------------------------------------------------------









#Five-Fold
fold=5
#Five-Fold of n times
n=10
kf=KFold(n_splits=fold, shuffle=False)
Wlin0_F=np.zeros(n*fold)
Wlin1_F=np.zeros(n*fold)
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
        y_regress_Five_Fold_test=np.zeros(len(test_index))
        for i in np.arange(0, len(train_index)):
            training_data_Fold[i]=x[train_index[i]]
        for i in np.arange(0, len(test_index)):
            testing_data_Fold[i]=x[test_index[i]]
        for i in np.arange(0, len(train_index)):
            y_Five_Fold[i]=linear_model(x[train_index[i]])
        for i in np.arange(0, len(test_index)):
            y_test[i]=linear_model(x[test_index[i]])
        s=(len(train_index),2)
        X_matrix=np.zeros(s)
        for i in np.arange(0, len(train_index)):
            X_matrix[i][0]=training_data_Fold[i]
            X_matrix[i][1]=1

        X_matrix_T=X_matrix.transpose()
        X_inverse=np.linalg.inv(X_matrix_T.dot(X_matrix))
        X_total=X_inverse.dot(X_matrix_T)
        #Five=Fold model
        Wlin=X_total.dot(y_Five_Fold)
        y_regress_Five_Fold_test=Wlin[0]*testing_data_Fold+Wlin[1]
        testing_Five_Fold_error[g][a]=mean_squared_error(y_test, y_regress_Five_Fold_test)
        #print(Wlin[0])
        Wlin0_F[a+fold*g]=Wlin[0]
        Wlin1_F[a+fold*g]=Wlin[1]
        
        a=a+1
mean_squared_FiveFold=str(np.average(testing_Five_Fold_error.flatten()))
print("Five-Fold: ", mean_squared_FiveFold)
#average weighting of New Model
y_regress_Five_Fold=np.average(Wlin0_F)*x+np.average(Wlin1_F)

plt.scatter(x, y, color="black", label="linear model", s=60)
plt.plot(x, y_regress, color="red", label="traning model", linewidth=5)
plt.plot(x, y_regress_LOOCV, color="green", label="leave-one-out", linewidth=2.5)
plt.plot(x, y_regress_Five_Fold, color="blue", label="Five-Fold", linewidth=1.5)
plt.text(0.85, 1.8, "training error: "+training_error, fontsize=15)
plt.text(0.85, 1.2, "testing error: "+testing_error, fontsize=15)
plt.text(0.85, 0.6, "Leave-one-out error: "+mean_squared_LOOCV, fontsize=15)
plt.text(0.85, 0.0, "Five-Fold error: "+mean_squared_FiveFold, fontsize=15)
plt.legend()
plt.show()

