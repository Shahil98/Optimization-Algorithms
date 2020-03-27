import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math

#Gradient Descent
class GD:
    def __init__(self,X,lr):
        self.X = X
        self.X_arr = []
        self.X_arr.append(X)
        self.lr = lr
        self.level_sets = []
        self.min_prog_x = []
        self.cnt = 1
        self.del_fx = np.ones((2,1))
        self.fx()
    def fx(self):
        val = round(math.pow(self.X[1][0] - self.X[0][0],4) + 12*self.X[0][0]*self.X[1][0] + self.X[1][0] - self.X[0][0] - 3,2)
        #print(val)
        self.level_sets.append(val)
        self.min_prog_x.append(self.cnt)
        self.cnt = self.cnt + 1
    def fx_return(self,x1,x2):
        return np.power(x2-x1,4)+(12*x1*x2)-x1+x2-3
    def gradient(self):
        self.del_fx[0][0] = round(-(4*(self.X[1][0]-self.X[0][0])*(self.X[1][0]-self.X[0][0])*(self.X[1][0]-self.X[0][0])) - 1 + (12*self.X[1][0]),2)
        self.del_fx[1][0] = round((4*(self.X[1][0]-self.X[0][0])*(self.X[1][0]-self.X[0][0])*(self.X[1][0]-self.X[0][0])) + 1 + (12*self.X[0][0]),2)
        return self.del_fx
    def cal_minimizer(self):
        prev_fx = 1
        cur_fx = 2
        while(prev_fx != cur_fx):
            if(self.cnt == 1 or self.cnt == 2):
                prev_fx = 1
                cur_fx = 2
            else:
                prev_fx = self.level_sets[self.cnt - 2]
                cur_fx = self.level_sets[self.cnt - 3]
            self.X = np.subtract(self.X,self.lr*self.gradient())
            self.X[1][0] = round(self.X[1][0],2)
            self.X[0][0] = round(self.X[0][0],2)
            self.fx()
            self.X_arr.append(self.X)
    def plot_graph(self):
        plt.plot(self.min_prog_x,self.level_sets)
        plt.scatter(self.min_prog_x,self.level_sets,color='red')
        plt.show()
        x1 = []
        x2 = []
        self.X_arr = np.array(self.X_arr)
        for i in range(len(self.level_sets)):
            x1.append(self.X_arr[i][0][0])
            x2.append(self.X_arr[i][1][0])
        X = np.linspace(-1,1,30)
        Y = np.linspace(-1,1,30)
        X,Y = np.meshgrid(X,Y)
        Z = self.fx_return(X,Y)
        plt.contour(X,Y,Z,colors='black')
        plt.plot(x1,x2,color='blue')
        plt.scatter(x1,x2,color='red')
        plt.show()
"""
#Steepest Descent
class SD:
    def __init__(self,X):
        self.X = X
        self.level_sets = []
        self.min_prog_x = []
        self.X_arr = [] 
        self.del_fx = np.ones((2,1))
        self.cnt = 1
        self.lr = 5
    def gradient(self):
        self.del_fx[0][0] = round(-(4*(self.X[1][0]-self.X[0][0])*(self.X[1][0]-self.X[0][0])*(self.X[1][0]-self.X[0][0])) - 1 + (12*self.X[1][0]),2)
        self.del_fx[1][0] = round((4*(self.X[1][0]-self.X[0][0])*(self.X[1][0]-self.X[0][0])*(self.X[1][0]-self.X[0][0])) + 1 + (12*self.X[0][0]),2)
        return self.del_fx
    def fx(self):
        val = round(math.pow(self.X[1][0] - self.X[0][0],4) + 12*self.X[0][0]*self.X[1][0] + self.X[1][0] - self.X[0][0] - 3,2)
        self.level_sets.append(val)
        self.min_prog_x.append(self.cnt)
        self.cnt = self.cnt + 1
    def fx_return(self,x1,x2):
        return np.power(x2-x1,4)+(12*x1*x2)-x1+x2-3
    def cal_lr(self):
        f_dash_lr = 1
        f_ddash_lr = 1
        while(round(f_dash_lr/f_ddash_lr,2)>0):
            y1 = - round(4*math.pow(self.X[1][0]-self.X[0][0],3) + 12*self.X[1][0] - 1,2)
            y2 = round(4*math.pow(self.X[1][0]-self.X[0][0],3) + 12*self.X[0][0] + 1,2)
            f_dash_lr = round(4*(self.X[1][0]-(self.lr*y2) - self.X[0][0] + self.lr*y1)*(self.X[1][0]-(self.lr*y2) - self.X[0][0] + self.lr*y1)*(self.X[1][0]-(self.lr*y2) - self.X[0][0] + self.lr*y1)*(y1 - y2) - 12*y1*(self.X[1][0]-(self.lr*y2)) - 12*y2*(self.X[0][0]-self.lr*y1) + y1 - y2,1)
            f_ddash_lr = round(12*(self.X[1][0]-(self.lr*y2)-self.X[0][0] + (self.lr*y1))*(self.X[1][0]-(self.lr*y2)-self.X[0][0] + (self.lr*y1))*(y1-y2)*(y1-y2) + 24*y1*y2,2)
            self.lr = round(self.lr - (f_dash_lr/f_ddash_lr),2)
            #print("lr:",self.lr,"f_dash_lr:",f_dash_lr,"f_ddash_lr:",f_ddash_lr)
        #print("------------------------------------------------")
    def cal_minimizer(self):
        count = 0
        while(count<50):
            count = count + 1
            self.lr = 0.003
            self.cal_lr()
            self.X = np.subtract(self.X,self.lr*self.gradient())
            self.X[1][0] = round(self.X[1][0],2)
            self.X[0][0] = round(self.X[0][0],2)
            self.fx()
            self.X_arr.append(self.X)
        print(self.X_arr)
    def fx_(self,X,Y):
        return np.power(Y - X,4) + 12*X*Y + Y - X - 3
    def plot_graph(self):
        #For F(x)
        plt.plot(self.min_prog_x,self.level_sets)
        plt.scatter(self.min_prog_x,self.level_sets,color='red')
        plt.show()
        x1 = []
        x2 = []
        print()
        for i in range(len(self.level_sets)):
            x1.append(self.X_arr[i][0][0])
            x2.append(self.X_arr[i][1][0])
        X = np.linspace(-1,1,30)
        Y = np.linspace(-1,1,30)
        X,Y = np.meshgrid(X,Y)
        Z = self.fx_return(X,Y)
        plt.contour(X,Y,Z,colors='black')
        plt.plot(x1,x2,color='blue')
        plt.scatter(x1,x2,color='red')
        plt.show()

"""
#Steepest Descent
class SD:
    def __init__(self,X):
        self.X = X
        self.X_arr = []
        self.level_sets = []
        self.min_prog_x = []
        self.cnt = 1
        self.del_fx = np.ones((2,1))
        self.Fx_inv = np.ones((2,2))
        self.lr = 1
        self.fd_lr = 1
        self.fdd_lr = 1
    def fx(self):
        val = round(math.pow(self.X[1][0] - self.X[0][0],4) + 12*self.X[0][0]*self.X[1][0] + self.X[1][0] - self.X[0][0] - 3,2)
        self.X_arr.append(self.X)
        self.level_sets.append(val)
        self.min_prog_x.append(self.cnt)
        self.cnt = self.cnt + 1

    def fx_return(self,x1,x2):
        return np.power(x2-x1,4)+(12*x1*x2)-x1+x2-3

    def gradient(self):
        self.del_fx[0][0] = round(-(4*(self.X[1][0]-self.X[0][0])*(self.X[1][0]-self.X[0][0])*(self.X[1][0]-self.X[0][0])) - 1 + (12*self.X[1][0]),2)
        self.del_fx[1][0] = round((4*(self.X[1][0]-self.X[0][0])*(self.X[1][0]-self.X[0][0])*(self.X[1][0]-self.X[0][0])) + 1 + (12*self.X[0][0]),2)

    def cal_lr(self):
        prev_lr = 10
        while((round(prev_lr,2) - round(self.lr,2))>0.1):
            prev_lr = self.lr
            self.fd_lr = round(4*((self.lr*(self.del_fx[1][0]-self.del_fx[0][0]) + self.X[0][0]-self.X[1][0])**3)*(self.del_fx[1][0]-self.del_fx[0][0]) + 12*(2*self.lr*self.del_fx[1][0]*self.del_fx[0][0] - self.del_fx[0][0]*self.X[1][0] - self.del_fx[1][0]*self.X[0][0]) + self.del_fx[0][0] - self.del_fx[1][0],2)
            self.fdd_lr = round(12*((self.lr*(self.del_fx[1][0]-self.del_fx[0][0]) + self.X[0][0]-self.X[1][0])**2)*((self.del_fx[1][0]-self.del_fx[0][0])**2) + 24*self.del_fx[1][0]*self.del_fx[0][0],2) 
            self.lr = round(self.lr - (self.fd_lr/self.fdd_lr),2)

    def cal_minimizer(self):
        self.fx()
        prev_x = np.ones((2,1))
        norm = math.sqrt((self.X[0][0]-prev_x[0][0])**2 + (self.X[1][0]-prev_x[1][0])**2)
        while(norm>0.1):
            prev_x = self.X
            self.lr = 0.5
            self.gradient()
            self.cal_lr()
            self.X = np.subtract(self.X,self.lr*self.del_fx)
            self.fx()
            norm = math.sqrt((self.X[0][0]-prev_x[0][0])**2 + (self.X[1][0]-prev_x[1][0])**2)
    def plot_graph(self):
        plt.plot(self.min_prog_x,self.level_sets)
        plt.scatter(self.min_prog_x,self.level_sets,color='red')
        plt.show()
        x1 = []
        x2 = []
        self.X_arr = np.array(self.X_arr)
        for i in range(len(self.level_sets)):
            x1.append(self.X_arr[i][0][0])
            x2.append(self.X_arr[i][1][0])
        X = np.linspace(-1,1,50)
        Y = np.linspace(-1,1,50)
        X,Y = np.meshgrid(X,Y)
        Z = self.fx_return(X,Y)
        plt.contour(X,Y,Z,colors='black')
        plt.plot(x1,x2,color='blue')
        plt.scatter(x1,x2,color='red')
        plt.show()
#Newtons Method
class NM:
    def __init__(self,X):
        self.X = X
        self.X_arr = []
        self.level_sets = []
        self.min_prog_x = []
        self.cnt = 1
        self.del_fx = np.ones((2,1))
        self.Fx_inv = np.ones((2,2))
    def fx(self):
        val = round(math.pow(self.X[1][0] - self.X[0][0],4) + 12*self.X[0][0]*self.X[1][0] + self.X[1][0] - self.X[0][0] - 3,2)
        self.X_arr.append(self.X)
        self.level_sets.append(val)
        self.min_prog_x.append(self.cnt)
        self.cnt = self.cnt + 1
    def fx_return(self,x1,x2):
        return np.power(x2-x1,4)+(12*x1*x2)-x1+x2-3
    def gradient(self):
        self.del_fx[0][0] = round(-(4*(self.X[1][0]-self.X[0][0])*(self.X[1][0]-self.X[0][0])*(self.X[1][0]-self.X[0][0])) - 1 + (12*self.X[1][0]),2)
        self.del_fx[1][0] = round((4*(self.X[1][0]-self.X[0][0])*(self.X[1][0]-self.X[0][0])*(self.X[1][0]-self.X[0][0])) + 1 + (12*self.X[0][0]),2)

    def cal_Fx(self):
        self.Fx_inv[0][0] = round(12*((self.X[1][0]-self.X[0][0])**2),2)
        self.Fx_inv[1][1] = round(12*((self.X[1][0]-self.X[0][0])**2),2)
        self.Fx_inv[1][0] = round(12*((self.X[1][0]-self.X[0][0])**2) - 12,2)
        self.Fx_inv[0][1] = round(12*((self.X[1][0]-self.X[0][0])**2) - 12,2)
        det = round((12*((self.X[1][0]-self.X[0][0])**2))**2 - (12-(12*((self.X[1][0]-self.X[0][0])**2)))**2,2)
        self.Fx_inv = self.Fx_inv/det
    def cal_minimizer(self):
        self.fx()
        prev_x = np.ones((2,1))
        norm = math.sqrt((self.X[0][0]-prev_x[0][0])**2 + (self.X[1][0]-prev_x[1][0])**2)
        while(norm>0.01):
            prev_x = self.X
            self.gradient()
            self.cal_Fx()
            self.X = np.subtract(self.X,np.matmul(self.Fx_inv,self.del_fx))
            self.fx()
            norm = math.sqrt((self.X[0][0]-prev_x[0][0])**2 + (self.X[1][0]-prev_x[1][0])**2)
    def plot_graph(self):
        plt.plot(self.min_prog_x,self.level_sets)
        plt.scatter(self.min_prog_x,self.level_sets,color='red')
        plt.show()
        x1 = []
        x2 = []
        self.X_arr = np.array(self.X_arr)
        for i in range(len(self.level_sets)):
            x1.append(self.X_arr[i][0][0])
            x2.append(self.X_arr[i][1][0])
        X = np.linspace(-1,1,50)
        Y = np.linspace(-1,1,50)
        X,Y = np.meshgrid(X,Y)
        Z = self.fx_return(X,Y)
        plt.contour(X,Y,Z,colors='black')
        plt.plot(x1,x2,color='blue')
        plt.scatter(x1,x2,color='red')
        plt.show()

X1 = np.zeros((2,1))
X1[0][0] = 0.55
X1[1][0] = 0.7

X2 = np.zeros((2,1))
X2[0][0] = -0.9
X2[1][0] = -0.5

gd_1 = GD(X1,0.02)
gd_1.cal_minimizer()
gd_1.plot_graph()
print("Answer of GD:",gd_1.X_arr[len(gd_1.X_arr)-1])
print(len(gd_1.X_arr),len(gd_1.level_sets))
print("X:",gd_1.X_arr)
print("level_sets : ",gd_1.level_sets)

gd_2 = GD(X2,0.02)
gd_2.cal_minimizer()
gd_2.plot_graph()
print("Answer of GD:",gd_2.X_arr[len(gd_2.X_arr)-1])

print("X:",gd_2.X_arr)
print("level_sets : ",gd_2.level_sets)

sd_1 = SD(X1)
sd_1.cal_minimizer()
sd_1.plot_graph()


sd_2 = SD(X2)
sd_2.cal_minimizer()
sd_2.plot_graph()



nm_1 = NM(X1)
nm_1.cal_minimizer()
nm_1.plot_graph()

nm_2 = NM(X2)
nm_2.cal_minimizer()
nm_2.plot_graph()

