import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math

#Newtons Method
class NM:
    """
    Following function initializes the required variables and lists.
    """
    def __init__(self,X):
        self.X = X
        self.X_arr = []
        self.level_sets = []
        self.min_prog_x = []
        self.cnt = 1
        self.del_fx = np.ones((2,1))
        self.Fx_inv = np.ones((2,2))
    
    """
    Following function calculates the function value and adds it to the level_sets list.
    """
    def fx(self):
        val = round(math.pow(self.X[1][0] - self.X[0][0],4) + 12*self.X[0][0]*self.X[1][0] + self.X[1][0] - self.X[0][0] - 3,2)
        self.X_arr.append(self.X)
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

    """
    Following function returns an inverse of second derivative.
    """
    def cal_Fx(self):
        self.Fx_inv[0][0] = round(12*((self.X[1][0]-self.X[0][0])**2),2)
        self.Fx_inv[1][1] = round(12*((self.X[1][0]-self.X[0][0])**2),2)
        self.Fx_inv[1][0] = round(12*((self.X[1][0]-self.X[0][0])**2) - 12,2)
        self.Fx_inv[0][1] = round(12*((self.X[1][0]-self.X[0][0])**2) - 12,2)
        det = round((12*((self.X[1][0]-self.X[0][0])**2))**2 - (12-(12*((self.X[1][0]-self.X[0][0])**2)))**2,2)
        self.Fx_inv = self.Fx_inv/det
    
    """
    Following function minimizes the given function.
    """
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
    
    """
    Following function plots a contour plot.
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
        X = np.linspace(-1,1,50)
        Y = np.linspace(-1,1,50)
        X,Y = np.meshgrid(X,Y)
        Z = self.fx_return(X,Y)
        plt.contour(X,Y,Z,colors='black')
        plt.plot(x1,x2,color='blue')
        plt.scatter(x1,x2,color='red')
        plt.title("Contour plot which shows that NM gets stuck")
        plt.show()

"""
Following piece of code initializes required variables and two NM objects and than performs minimization.
"""
X1 = np.zeros((2,1))
X1[0][0] = 0.55
X1[1][0] = 0.7

X2 = np.zeros((2,1))
X2[0][0] = -0.9
X2[1][0] = -0.5

nm_1 = NM(X1)
nm_1.cal_minimizer()
nm_1.plot_graph()
print("Answer of Newton's method:",nm_1.X_arr[len(nm_1.X_arr)-1])

nm_2 = NM(X2)
nm_2.cal_minimizer()
nm_2.plot_graph()
print("Answer of Newton's method:",nm_2.X_arr[len(nm_2.X_arr)-1])