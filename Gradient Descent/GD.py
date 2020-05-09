import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math

#Gradient Descent
class GD:
    """
    Following function initializes the required variables and lists.
    """
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
    
    """
    Following function calculates the function value and adds it to the level_sets list.
    """
    def fx(self):
        val = round(math.pow(self.X[1][0] - self.X[0][0],4) + 12*self.X[0][0]*self.X[1][0] + self.X[1][0] - self.X[0][0] - 3,2)
        self.level_sets.append(val)
        self.min_prog_x.append(self.cnt)
        self.cnt = self.cnt + 1
    
    """
    Following function returns function values at all specified values in list x1 and x2.
    """
    def fx_return(self,x1,x2):
        return np.power(x2-x1,4)+(12*x1*x2)-x1+x2-3
    
    """
    Following function calculates and returns a gradient value at a point.
    """
    def gradient(self):
        self.del_fx[0][0] = round(-(4*(self.X[1][0]-self.X[0][0])*(self.X[1][0]-self.X[0][0])*(self.X[1][0]-self.X[0][0])) - 1 + (12*self.X[1][0]),2)
        self.del_fx[1][0] = round((4*(self.X[1][0]-self.X[0][0])*(self.X[1][0]-self.X[0][0])*(self.X[1][0]-self.X[0][0])) + 1 + (12*self.X[0][0]),2)
        return self.del_fx
    
    """
    Following function is used to minimize the given function.
    """
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
    
    """
    Following function is used to plot a contour and also the function value at each iteration.
    """
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
        plt.title("Contour plot for start point : ("+str(self.X_arr[0][0][0])+","+str(self.X_arr[0][1][0]) + ")")
        plt.show()


"""
Following piece of code initializes required parameters and two gradient descent objects and than minimizes the function.
"""
Learning_rate = 0.02

X1 = np.zeros((2,1))
X1[0][0] = 0.55
X1[1][0] = 0.7

X2 = np.zeros((2,1))
X2[0][0] = -0.9
X2[1][0] = -0.5

gd_1 = GD(X1,Learning_rate)
gd_1.cal_minimizer()
gd_1.plot_graph()
print("Answer of GD:",gd_1.X_arr[len(gd_1.X_arr)-1])
print(len(gd_1.X_arr),len(gd_1.level_sets))
print("X:",gd_1.X_arr)
print("level_sets : ",gd_1.level_sets)

gd_2 = GD(X2,Learning_rate)
gd_2.cal_minimizer()
gd_2.plot_graph()
print("Answer of GD:",gd_2.X_arr[len(gd_2.X_arr)-1])

print("X:",gd_2.X_arr)
print("level_sets : ",gd_2.level_sets)


