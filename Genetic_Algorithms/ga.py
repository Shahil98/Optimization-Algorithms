"""
Importing necessRY LIBRARIES.
"""
import numpy as np
import random
import matplotlib.pyplot as plt

"""
Following function is the function to be minimized.
"""
def func(x1,x2):
    return((x2-x1)**4 + 12*x1*x2 + x2 - x1 - 3)

"""
Following class is to define a chromosome/node.
"""
class Node():
    def __init__(self):
        self.X = np.random.uniform(low = -1, high = 1, size = (2,1))
        self.X_bin = ""
        self.f_val = func(self.X[0][0],self.X[1][0])
        self.fitness = None

class GA():
    """
    Following function initializes population for the first generation.
    """
    def __init__(self,epochs,pop_num):
        if(int(pop_num/2)%2 != 0):
            pop_num += 2
        self.f_max = None
        self.population = []
        for i in range(pop_num):
            self.population.append(Node())
        self.epochs = epochs
        self.best = []
        self.worst = []
        self.average = []
    
    """
    Following function calculates the maximum f_value i.e. function value among all the nodes/chromosomes in the population.
    """
    def cal_f_max(self):
        self.f_max = self.population[0].f_val
        for i in range(1,len(self.population)):
            if(self.f_max<self.population[i].f_val):
                self.f_max = self.population[i].f_val
    
    """
    Foolowing function calculates the fitness value for each node/chromosome.
    """
    def cal_fitness(self):
        for i in range(len(self.population)):
            self.population[i].fitness = round(self.f_max - self.population[i].f_val,4)
    
    """
    Following function is used to calculate a binary representation of x and y coordinates for each node/chromosome.
    """
    def cal_X_bin(self):
        for i in range(len(self.population)):
            x1 = self.population[i].X[0][0] 
            x2 = self.population[i].X[1][0]
            x1 = int((x1 + 1)*1000)
            x2 = int((x2 + 1)*1000)
            x1_bin = '{0:11b}'.format(x1)
            x2_bin = '{0:11b}'.format(x2)
            j = 0
            while(x1_bin[j]==' '):
                x1_bin = x1_bin[0:j] + "0" + x1_bin[j+1:]
                j = j+1
            j = 0
            while(x2_bin[j] == ' '):
                x2_bin = x2_bin[0:j] + "0" + x2_bin[j+1:]
                j = j+1
            self.population[i].X_bin = x1_bin + x2_bin

    """
    Following function is used to convert a binary representation into x and y coordinates.
    """
    def cal_int(self,x_bin):
        x1 = x_bin[:11]
        x2 = x_bin[11:]
        x1 = int(x1,2)
        x1 = x1/1000
        x1 = x1 - 1
        x2 = int(x2,2)
        x2 = x2/1000
        x2 = x2 - 1
        return(x1,x2)
    
    """
    Following function is used to select candidates such that nodes/chromosomes having high fitness have higher probability of getting selected. For this roullete selection technique is applied.
    """
    def roullete_selection(self):
        l = len(self.population)/2
        for i in range(int(l)):
            sum = 0
            for j in range(len(self.population)):
                sum = round(sum + self.population[j].fitness,4)
            if(sum < 1):
                rand_num = 0
            else:
                rand_num = np.random.randint(0,int(sum))
            k = 0
            sum = 0
            while(sum<rand_num):
                sum = sum + self.population[k].fitness
                k = k + 1
            if(k == 0):
                self.M.append(self.population.pop(0))
            else:
                self.M.append(self.population.pop(k-1))

    """
    Following function is used to perform cross-over between the candidates generated.
    """
    def cross_over(self):
        M_new = []
        while(len(self.M) != 0):
            p1 = self.M.pop(np.random.randint(0,len(self.M)))
            p2 = self.M.pop(np.random.randint(0,len(self.M)))
            of_1_bin = p1.X_bin
            of_2_bin = p2.X_bin
            p_c = np.random.randint(1,4)
            if(p_c == 2):
                x = np.random.randint(0,22)
                of_1_bin_new = of_1_bin[0:x] + of_2_bin[x:]
                of_2_bin_new = of_2_bin[0:x] + of_1_bin[x:]
                of_1_bin = of_1_bin_new
                of_2_bin = of_2_bin_new
            M_new.append(p1)
            M_new.append(p2)
            of_node_1 = Node()
            of_node_1.X_bin = of_1_bin
            of_node_2 = Node()
            of_node_2.X_bin = of_2_bin
            of_node_1.X[0][0],of_node_1.X[1][0] = self.cal_int(of_node_1.X_bin)
            of_node_2.X[0][0],of_node_2.X[1][0] = self.cal_int(of_node_2.X_bin)
            of_node_1.f_val = func(of_node_1.X[0][0],of_node_1.X[1][0])
            of_node_2.f_val = func(of_node_2.X[0][0],of_node_2.X[1][0])
            M_new.append(of_node_1)
            M_new.append(of_node_2)
        return(M_new)
    
    """
    Following function is used to perform a random mutation for each node/crossover present in the population list.
    """
    def mutate(self):
        for i in range(len(self.population)):
            for j in range(22):
                rand_num = np.random.randint(1,25)
                if(rand_num == 5):
                    if(self.population[i].X_bin[j] == "0"):
                        self.population[i].X_bin= self.population[i].X_bin[0:j] + "1" + self.population[i].X_bin[j+1:]
                    else: 
                        self.population[i].X_bin= self.population[i].X_bin[0:j] + "0" + self.population[i].X_bin[j+1:]
            self.population[i].X[0][0],self.population[i].X[1][0] = self.cal_int(self.population[i].X_bin)
            self.population[i].f_val = func(self.population[i].X[0][0],self.population[i].X[1][0])
    
    """
    Following function is used to minimize the given function.
    """
    def minimize(self):
        for i in range(self.epochs):
            self.cal_f_max()
            self.cal_fitness()
            self.cal_X_bin()
            self.M = []
            self.roullete_selection()
            self.population = self.cross_over()
            self.mutate()   
            best_curr = 999999
            average_curr = 0
            worst_curr = -999999
            for j in range(len(self.population)):
                average_curr = average_curr + self.population[j].f_val
                if(best_curr>self.population[j].f_val):
                    best_curr = self.population[j].f_val
                if(worst_curr<self.population[j].f_val):
                    worst_curr = self.population[j].f_val
            self.best.append(best_curr)
            self.worst.append(worst_curr)
            self.average.append(average_curr/(len(self.population)))
        min = self.population[0].f_val 
        min_point = self.population[0].X
        for i in range(1,len(self.population)):
            if(min>self.population[i].f_val):
                min = self.population[i].f_val
                min_point = self.population[i].X
        print("Minimum objective value : ",min,"Minimizer point : ",min_point)

    """
    Following function is used to plot the best, average and worst function values in each generation.
    """
    def graph_plot(self):
        X = []
        for i in range(self.epochs):
            X.append(i+1)
        plt.plot(X,self.best,color='green')
        plt.scatter(X,self.best,color='green')
        plt.plot(X,self.average,color='blue')
        plt.scatter(X,self.average,color='blue')
        plt.plot(X,self.worst,color='red')
        plt.scatter(X,self.worst,color='red')
        plt.xlabel('Generation')
        plt.ylabel('Function value')
        plt.title('Best, average and worst function values in each generation')
        plt.show()

"""
Following piece of code initializes a GA object, minimizes the function based on passed parameters during initialization and than plots a graph for the best, average and worst function values in each generation.
"""
poulation_size = 50
Generations = 50
g = GA(Generations,poulation_size)
g.minimize()
g.graph_plot()
