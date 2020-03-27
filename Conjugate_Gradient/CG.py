import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class c_grad:

    def __init__(self,X,Q):
        self.X = X
        self.alpha = 1
        self.beta = 1
        self.d = np.ones((2,1))
        self.Q = Q
        self.del_fx = np.ones((2,1))
        self.X_arr = []
        self.level_sets = []

    def cal_fx(self):
        return (self.X[0][0]**2 + self.X[1][0]**2 + self.X[0][0]*self.X[1][0] - 3*self.X[0][0])
    
    def cal_grad(self):
        self.del_fx[0][0] = 2*self.X[0][0] + self.X[1][0] - 3
        self.del_fx[1][0] = 2*self.X[1][0] + self.X[0][0] 
        return self.del_fx
    
    def cal_alpha(self):
        self.alpha = - (np.matmul(self.cal_grad().transpose(),self.d)[0][0]
        /np.matmul(np.matmul(self.d.transpose(),self.Q),self.d)[0][0])
        return self.alpha

    def cal_beta(self):
        self.beta = (np.matmul(np.matmul(self.cal_grad().transpose(),self.Q),self.d)[0][0]
        /np.matmul(np.matmul(self.d.transpose(),self.Q),self.d)[0][0])
        return self.beta
    
    def cal_dir(self):
        self.d = self.cal_beta()*self.d - self.cal_grad()
    
    def minimize(self):
        self.level_sets.append(self.cal_fx())
        self.X_arr.append(self.X)
        for i in range(0,2):
            if(i == 0):
                self.d = - self.cal_grad()
            else:
                self.cal_dir()
                print("beta ",i," : ",self.beta)
                print("g ",i," : ",self.del_fx)
            self.X = self.X + self.cal_alpha()*self.d
            print("alpha",i," : ",self.alpha)
            self.level_sets.append(self.cal_fx())
            self.X_arr.append(self.X)
            print("d ",i," : ",self.d)
        print("X_Values : ",self.X_arr)
        print("Level Sets : ",self.level_sets)
    def fx_contour(self,x1,x2):
        return np.power(x1,2)+np.power(x2,2)+(x1*x2) - (3*x1)

    def plot_graph(self):
        x1 = []
        x2 = []
        for i in range(len(self.level_sets)):
            x1.append(self.X_arr[i][0][0])
            x2.append(self.X_arr[i][1][0])
        cnt_arr = []
        for i in range(len(self.level_sets)):
            cnt_arr.append(i+1)
        plt.plot(cnt_arr,self.level_sets,color='blue')
        plt.scatter(cnt_arr,self.level_sets,color='red')
        plt.show()
        X = np.linspace(-20,20,50)
        Y = np.linspace(-20,20,50)
        X,Y = np.meshgrid(X,Y)
        Z = self.fx_contour(X,Y)
        plt.contour(X,Y,Z,colors='black')
        plt.plot(x1,x2,color='blue')
        plt.scatter(x1,x2,color='red')
        plt.show()

X = np.zeros((2,1))
X[0][0] = 0
X[1][0] = 0
Q = np.ones((2,2))
Q[0][1] = 1
Q[1][0] = 1
Q[1][1] = 2
Q[0][0] = 2
obj = c_grad(X,Q)
obj.minimize()
obj.plot_graph()