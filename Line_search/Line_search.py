import math
import matplotlib.pyplot as plt
import random
import numpy as np
import pandas as pd
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
class LS:

    def __init__(self,X,method):
        self.method = method
        self.X = X
        self.epsilon = 0.075
        self.un_region = 0.01
        self.a = 1
        self.golden_section_arr = []
        #self.fib_arr = []
        self.X1 = np.ones((10,2))
        self.X2 = np.ones((10,2))
        self.Z = np.ones((10,2))

    #Function    
    def fx(self,x1,x2):
        return round(x2**2 + x1**2 + x1*x2,3)
    def fx_bracket_selection(self):
        self.a = self.X
        self.b = self.X + self.epsilon
        self.c = self.X + 2*self.epsilon
        count = 0
        temp = 0
        while(temp == 0):
            self.epsilon = 2*self.epsilon
            if(self.fx(self.a[0][0],self.a[1][0])>self.fx(self.b[0][0],self.b[1][0]) and 
            self.fx(self.c[0][0],self.c[1][0])<self.fx(self.b[0][0],self.b[1][0])):
                self.a = self.b
                self.b = self.c
                self.c = self.c + self.epsilon
            elif(self.fx(self.c[0][0],self.c[1][0])>self.fx(self.b[0][0],self.b[1][0]) and 
            self.fx(self.a[0][0],self.a[1][0])<self.fx(self.b[0][0],self.b[1][0])):
                self.c = self.b
                self.b = self.a
                self.a = self.a - self.epsilon
            else:
                temp = 1
        print("Bracketing Procedure Brackets :","a - ",self.a,"  b - ",self.c)
    def golden_section_search(self):
        count = 0
        arr = []
        norm = round(math.sqrt((self.c[0][0]-self.a[0][0])**2 + (self.c[1][0]-self.a[1][0])**2),3)
        self.golden_section_arr.append([self.a,self.c])
        self.X1[count][0] = self.a[0][0]
        self.X1[count][1] = self.c[0][0]
        self.X2[count][0] = self.a[1][0]
        self.X2[count][1] = self.c[1][0]
        self.Z[count][0] = count + 1
        self.Z[count][1] = count + 1
        while(norm>self.un_region):
            print("Iteration : ",count+1)
            if(count == 0):
                s = self.a + (1-0.618)*(self.c - self.a)
                t = self.a + (0.618)*(self.c-self.a)
            if(self.fx(s[0][0],s[1][0])<=self.fx(t[0][0],t[1][0])):
                self.c = t
                t = s
                s = self.a + (1-0.618)*(self.c-self.a)
            else:
                self.a = s
                s = t
                t = self.a + 0.618*(self.c-self.a)
            s[0][0] = round(s[0][0],3)
            s[1][0] = round(s[1][0],3)
            t[0][0] = round(t[0][0],3)
            t[1][0] = round(t[1][0],3)
            self.a[0][0] = round(self.a[0][0],3)
            self.a[1][0] = round(self.a[1][0],3)
            self.c[0][0] = round(self.c[0][0],3)
            self.c[1][0] = round(self.c[1][0],3) 
            count = count + 1
            norm = round(math.sqrt((self.c[0][0]-self.a[0][0])**2 + (self.c[1][0]-self.a[1][0])**2),3)
            print("a:",self.a," ","b:",self.c)
            print("f(a):",self.fx(self.a[0][0],self.a[1][0])," ","f(b):",self.fx(self.c[0][0],self.c[1][0]))
            print("Range : ",norm)
            print()
            print()
            self.golden_section_arr.append([self.a,self.c])    
            self.X1[count][0] = self.a[0][0]
            self.X1[count][1] = self.c[0][0]
            self.X2[count][0] = self.a[1][0]
            self.X2[count][1] = self.c[1][0]
            self.Z[count][0] = count + 1
            self.Z[count][1] = count + 1

    def graph_plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax = fig.gca(projection='3d')
        
        for i in range(10):
            ax.plot(self.X1[i],self.X2[i],self.Z[i])
        
        if(self.method == "GS"):
            plt.title('Golden Section Range Reduction')
        else:
            plt.title('Fibonacci Range Reduction')
        plt.legend(loc=2)
        plt.show()
        
    def fib_search(self):
        count = 0
        arr = []
        f_prev_1 = 1
        f_prev_2 = 1
        f_cur = f_prev_1 
        fib_arr = []
        fib_arr.append(f_cur)
        norm = math.sqrt((self.c[0][0]-self.a[0][0])**2 + (self.c[1][0]-self.a[1][0])**2)
        #self.fib_arr.append([self.a,self.c])
        while((1.2/f_cur)>(0.01/norm)): 
            f_cur = f_prev_1 + f_prev_2
            f_prev_1 = f_prev_2
            f_prev_2 = f_cur
            fib_arr.append(f_cur)
            count = count + 1
        count = 0
        print(fib_arr)
        self.X1[count][0] = self.a[0][0]
        self.X1[count][1] = self.c[0][0]
        self.X2[count][0] = self.a[1][0]
        self.X2[count][1] = self.c[1][0]
        self.Z[count][0] = count + 1
        self.Z[count][1] = count + 1
        arr = []
        n = len(fib_arr)-1
        fib_arr[0] = 1.2
        for i in range(len(fib_arr)-1):
            print("Iteration : ",count + 1)
            rho = round(1 - (fib_arr[n-i-1]/fib_arr[n-i]),3)
            if(count == 0):
                s = self.a + (rho)*(self.c - self.a)
                t = self.a + (1-rho)*(self.c-self.a)
            if(self.fx(s[0][0],s[1][0])<=self.fx(t[0][0],t[1][0])):
                self.c = t
                t = s
                s = self.a + (rho)*(self.c-self.a)
            else:
                self.a = s
                s = t
                t = self.a + (1-rho)*(self.c-self.a)
            s[0][0] = round(s[0][0],3)
            t[0][0] = round(t[0][0],3)
            s[1][0] = round(s[1][0],3)
            t[1][0] = round(t[1][0],3)
            self.a[0][0] = round(self.a[0][0],3)
            self.c[0][0] = round(self.c[0][0],3) 
            self.a[1][0] = round(self.a[1][0],3)
            self.c[1][0] = round(self.c[1][0],3)
            print(self.a,self.c)
            count = count + 1
            norm = math.sqrt((self.c[0][0]-self.a[0][0])**2 + (self.c[1][0]-self.a[1][0])**2)
            #print("a:",self.a," ","b:",self.c)
            #print("f(a):",self.fx(self.a[0][0],self.a[1][0])," ","f(b):",self.fx(self.a[0][0],self.a[1][0]))
            print("Range : ",norm)
            #print()
            #print()
            self.X1[count][0] = self.a[0][0]
            self.X1[count][1] = self.c[0][0]
            self.X2[count][0] = self.a[1][0]
            self.X2[count][1] = self.c[1][0]
            self.Z[count][0] = count + 1
            self.Z[count][1] = count + 1
            #self.fib_arr.append([self.a,self.c])

X = np.ones((2,1))
X[0][0] = 0.8
X[1][0] = -0.25
#ls_1 = LS(X,"GS")
#ls_1.fx_bracket_selection()
#ls_1.golden_section_search()
#ls_1.graph_plot()

ls_2 = LS(X,"FIB")
ls_2.fx_bracket_selection()
ls_2.fib_search()
ls_2.graph_plot()

