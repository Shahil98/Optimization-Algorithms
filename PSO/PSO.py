import numpy as np
import matplotlib.pyplot as plt


class function:

    def func(x):
        return((x[1][0]-x[0][0])**4 + 12*x[0][0]*x[1][0] - x[0][0] + x[1][0] - 3)

class particle(function):

    def __init__(self):
        self.x = np.random.rand(2,1)
        self.v = np.random.rand(2,1)
        self.p = self.x
        self.x_arr = []
        self.x_arr.append(self.x)
        self.level_set = []
        self.level_set.append(function.func(self.x))
    

class PSO(function):

    def __init__(self,epochs,d,w,c1,c2):
        self.swarm = []
        self.best = []
        self.worst = []
        self.average = []
        for i in range(d):
            par = particle()
            self.swarm.append(par)
        self.d = d
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.epochs = epochs
        self.g = None
        for i in range(d):
            if(i == 0):
                self.g = self.swarm[0].x
            elif(function.func(self.g)>function.func(self.swarm[i].x)):
                self.g = self.swarm[i].x
    
    def minimize(self):
        for i in range(self.epochs):
            for j in range(self.d):
                r = np.random.uniform(0.01,1,(2,1))
                s = np.subtract(np.ones((2,1)),r)
                #s = np.random.uniform(0.01,1,(2,1))
                self.swarm[j].v = np.add(np.add(np.multiply(self.w,self.swarm[j].v) , np.multiply(self.c1,np.multiply(r,np.subtract(self.swarm[j].p,self.swarm[j].x)))),np.multiply(self.c2,np.multiply(s,np.subtract(self.g,self.swarm[j].x))))
                self.swarm[j].x = self.swarm[j].x + self.swarm[j].v
                self.swarm[j].x_arr.append(self.swarm[j].x)
                self.swarm[j].level_set.append(function.func(self.swarm[j].x))
                if(function.func(self.swarm[j].x) < function.func(self.swarm[j].p)):
                    self.swarm[j].p = self.swarm[j].x
                worst_curr = -999999
                avg_curr = 0
                best_curr = 999999
            for j in range(self.d):
                if(function.func(self.swarm[j].x)<best_curr):
                    best_curr = function.func(self.swarm[j].x)
                if(function.func(self.swarm[j].x)>worst_curr):
                    worst_curr = function.func(self.swarm[j].x)
                avg_curr = avg_curr + function.func(self.swarm[j].x) 
                if(function.func(self.swarm[j].x) < function.func(self.g)):
                    self.g = self.swarm[j].x
            avg_curr = avg_curr/(self.d)
            self.best.append(best_curr)
            self.average.append(avg_curr)
            self.worst.append(worst_curr)
        print("minimum value : ",function.func(self.g),"minimizer point:",self.g)
                
    
    def fx_contour(self,x1,x2):
        return np.power(x2-x1,4)+(12*x1*x2)-x1+x2-3
     
    def plot(self):
        X = np.linspace(-1,1,50)
        Y = np.linspace(-1,1,50)
        X,Y = np.meshgrid(X,Y)
        Z = self.fx_contour(X,Y)
        plt.contour(X,Y,Z,colors='black')
        for j in range(self.d):
            x1 = []
            x2 = []
            self.swarm[0].x_arr = np.array(self.swarm[0].x_arr)
            for i in range(self.epochs + 1):
                x1.append(self.swarm[j].x_arr[i][0][0])
                x2.append(self.swarm[j].x_arr[i][1][0])
            plt.plot(x1,x2,color='blue')
            plt.scatter(x1,x2,color='red')
        plt.show()
        X = []
        for i in range(len(self.best)):
            X.append(i+1)
        plt.plot(X,self.best,color='green')
        plt.scatter(X,self.best,color='green')
        #plt.show()
        plt.plot(X,self.average,color='blue')
        plt.scatter(X,self.average,color='blue')
        #plt.show()
        plt.plot(X,self.worst,color='red')
        plt.scatter(X,self.worst,color='red')
        plt.show()
pso = PSO(20,14,0.8,1.8,1.8)
pso.minimize()
pso.plot()