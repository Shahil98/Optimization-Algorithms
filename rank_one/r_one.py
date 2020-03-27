import numpy as np
import matplotlib.pyplot as plt
import math
class r_one():

    def __init__(self,X):
        self.H = np.ones((2,2))
        self.H[1][0] = 0
        self.H[0][1] = 0
        self.X = X
        self.d = np.ones((2,1))
        self.g = np.ones((2,1))
        self.alpha = 0.2
        self.X_arr = []
        self.level_sets = []
    def fx(self,x1,x2):
        return ((x2-x1)**4 + 12*x2*x1 - x1 + x2 -3)

    def alpha_func(self,a):
        x1 = self.X[0][0] + self.d[0][0]*a
        x2 = self.X[1][0] + self.d[1][0]*a
        return (self.fx(x1,x2))

    def fx_return(self,x1,x2):
        return np.power(x2-x1,4)+(12*x1*x2)-x1+x2-3

    def search_alpha(self):
        epsilon = 0.05
        a = 0.0
        b = a + epsilon
        c = b + epsilon

        while(self.alpha_func(a)<self.alpha_func(b) or self.alpha_func(c)<self.alpha_func(b)):

            if(self.alpha_func(a)>self.alpha_func(b) and self.alpha_func(c)<self.alpha_func(b)):
                a = b
                b = c
                c = c + epsilon
            else:
                c = b
                b = a
                a = a - epsilon
            epsilon = epsilon*2

        b = c
        s = a + (1-0.618)*(b-a)
        t = a + 0.618*(b-a)
        while((b-a)>0.01):
            if(self.alpha_func(s)<self.alpha_func(t)):
                b = t
                t = s
                s = a + (b-a)*(1-0.618)
            else:    
                a = s
                s = t
                t = a + (b-a)*(0.618)
        return a
    def minimize(self):

        count = 0
        self.X_arr.append(self.X)
        self.level_sets.append(self.fx(self.X[0][0],self.X[1][0]))
        while( not np.array_equal(np.round(self.g,decimals=2),np.zeros((2,1)))):
            
            if(count == 0):
                self.g[0][0] = -4*(self.X[1][0]-self.X[0][0])**3 + 12*self.X[1][0] - 1
                self.g[1][0] = 4*(self.X[1][0]-self.X[0][0])**3 + 12*self.X[0][0] + 1
            prev_g = np.copy(self.g)
            self.g = np.round(self.g,decimals = 4)
 
            self.d = np.round( - np.matmul(self.H,self.g),decimals=4)

            self.alpha = self.search_alpha() 
            self.X = np.round(np.add(self.X,np.multiply(self.alpha,self.d)),decimals=4)

            ch_x = np.multiply(self.alpha,self.d)

            self.g[0][0] = -4*(self.X[1][0]-self.X[0][0])**3 + 12*self.X[1][0] - 1
            self.g[1][0] = 4*(self.X[1][0]-self.X[0][0])**3 + 12*self.X[0][0] + 1            
            ch_g = np.subtract(self.g,prev_g)
            self.H = np.add(self.H,np.divide(np.matmul(np.subtract(ch_x,np.matmul(self.H,ch_g)),np.subtract(ch_x,np.matmul(self.H,ch_g)).transpose()),np.matmul(ch_g.transpose(),np.subtract(ch_x,np.matmul(self.H,ch_g)))[0][0]))
            self.X_arr.append(self.X)
            self.level_sets.append(round(self.fx(self.X[0][0],self.X[1][0]),4))
            count = count + 1
        print(self.X_arr)
        print(self.level_sets)

    def plot_graph(self):
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
X1 = np.ones((2,1))
X1[0][0] = 0.55
X1[1][0] = 0.7
obj1 = r_one(X1)
obj1.minimize()
obj1.plot_graph()

X2 = np.ones((2,1))
X2[0][0] = -0.9
X2[1][0] = -0.5
obj2 = r_one(X2)
obj2.minimize()
obj2.plot_graph()