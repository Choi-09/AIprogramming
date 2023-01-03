import random
import math
from setup import Setup


class Problem(Setup):
    def __init__(self):
        Setup.__init__(self) # super().__init__()도 가능 
        self._solution = []
        self._value = 0
        self._numEval = 0

    def setVariables(self):
        pass
    
    def randomInit(self):
        pass

    def evaluate(self):
        pass

    def mutants(self):
        pass

    def randomMutant(self, current):
        pass

    def describe(self):
        pass

    def storeResult(self, solution, value):
        self._solution = solution
        self._value = value

    def report(self):
        print()
        print("Total number of evaluations: {0:,}".format(self._numEval))


class Numeric(Problem):
    def __init__(self):
        super().__init__()
        self._expression = ''
        self._domain = []
        self._delta = 0.01

    def setVariables(self):
        ## Read in a function and its domain from a file
        ## Then, set the relevant class variables
        fileName = input("Enter the file name of a function: ")
        infile = open(fileName, 'r')
        self._expression = infile.readline() # as a string
        varNames = []  # Variable names
        low = []       # Lower bounds
        up = []        # Upper bounds
        line = infile.readline()
        while line != '':
            data = line.split(',')  # read from CSV
            varNames.append(data[0])
            low.append(float(data[1]))
            up.append(float(data[2]))
            line = infile.readline()
        infile.close()
        self._domain = [varNames, low, up]


    def getDelta(self):
        return self._delta

    def randomInit(self): # Return a random initial point as a list
        low, up = self._domain[1], self._domain[2]
        init = []
        for i in range(len(low)):
            init.append(random.uniform(low[i], up[i]))
        return init

    def evaluate(self, current):
        self._numEval += 1
        varName = self._domain[0] # 여기에서 변수 명을 참조

        for i in range(len(varName)):
            cmd = varName[i] + '=' + str(current[i])
            exec(cmd)
        valueC = eval(self._expression)
        return valueC

    def mutants(self, current):
        neighbors = []
        for i in range(len(current)):
            m = self.mutate(current, i, self._delta)
            neighbors.append(m)
            m = self.mutate(current, i, -self._delta)
            neighbors.append(m)      
        return neighbors

    def mutate(self, current, i, d): ## Mutate i-th of 'current' if legal
        neighbor = current[:]
        low, up = self._domain[1], self._domain[2]
        if low[i] <= neighbor[i] + d <= up[i]:
            neighbor[i] += d
        return neighbor

    def randomMutant(self, current):
        # Pick a random locus
        i = random.randint(0, len(current) - 1)
        # Mutate the chosen locus
        if random.uniform(0, 1) > 0.5:
            d = self._delta
        else:
            d = -self._delta
        return self.mutate(current, i, d)

    def takeStep(self, x, v):
        grad = self.gradient(x, v)
        x_new = x[:]
        for i in range(len(x_new)):
            x_new[i] -= self._alpha*grad[i]
        if self.isLegal(x_new):
            return x_new
        else:
            return x

    def gradient(self, x, v):
        grad =[]
        # 각 x 마다
        for i in range(len(x)):
            x_new = x[:]
            x_new[i] += self._dx
            g = (self.evaluate(x_new)-v) / self._dx
            grad.append(g)     
        return grad
    
    def isLegal(self, x):
        domain = self._domain
        low = domain[1]
        up = domain[2]
        flag = True
        for i in range(len(low)):
            if x[i] < low[i] or up[i] < x[i]:
                flag = False
                break
        return flag

    def describe(self):
        print()
        print("Objective function:")
        # expression 출력
        print(self._expression)   # Expression
        print("Search space:")
        # Domain 정보 출력
        varNames = self._domain[0] # p[1] is domain: [VarNames, low, up]
        low = self._domain[1]
        up = self._domain[2]
        for i in range(len(low)):
            print(" " + varNames[i] + ":", (low[i], up[i]))

    def report(self):
        print()
        print("Solution found:")
        print(self.coordinate())  # Convert list to tuple
        print("Minimum value: {0:,.3f}".format(self._value))
        super().report()

    def coordinate(self):
        c = [round(value, 3) for value in self._solution]
        return tuple(c)  # Convert the list to a tuple

class Tsp(Problem):
    def __init__(self):
        super().__init__()
        self._numCities = 0
        self._locations = []
        self._distanceTable = []

    def setVariables(self):
        fileName = input("Enter the file name of a function: ")
        infile = open(fileName, 'r')
        self._numCities = int(infile.readline())
        self._locations = []
        line = infile.readline()
        while line != '':
            self._locations.append(eval(line))
            line = infile.readline()
        infile.close()
        self.calcDistanceTable()
    
    def calcDistanceTable(self):
        self._distanceTable = []
        for i in range(self._numCities):
            row = []
            for j in range(self._numCities):
                dx = self._locations[i][0] - self._locations[j][0]
                dy = self._locations[i][1] - self._locations[j][1]
                d = round(math.sqrt(dx**2 + dy**2), 1)
                row.append(d)
            self._distanceTable.append(row)

    def randomInit(self):
        init = list(range(self._numCities))
        random.shuffle(init)
        return init

    def evaluate(self, current):
        self._numEval += 1
        cost = 0
        for i in range(self._numCities-1):
            cost += self._distanceTable[current[i]][current[i+1]]
        return cost

    def mutants(self, current):
        neighbors = []
        triedPairs = []
        while len(neighbors) < self._numCities:
            i = random.randint(0, self._numCities-2)
            j = random.randint(i+1, self._numCities-1)
            if [i, j] in triedPairs:
                continue
            else:
                triedPairs.append([i, j])
            neighbors.append(self.inversion(current, i, j))
        return neighbors

    def inversion(self, current, i, j):
        curCopy = current[:]
        s = curCopy[i:j+1]
        s.reverse()
        curCopy[i:j+1] = s
        return curCopy

    def randomMutant(self, current): # Inversion only
        while True:
            i, j = sorted([random.randrange(self._numCities)
                           for _ in range(2)])
            if i < j:
                mutant = self.inversion(current, i, j)
                break
        return mutant

    def describe(self):
        print()
        print("Number of cities:", self._numCities)
        print("City locations:")
        for i in range(self._numCities):
            print("{0:>12}".format(str(self._locations[i])), end = '')
            if i % 5 == 4:
                print()

    def report(self):
        print()
        print("Best order of visits:")
        self.tenPerRow()       # Print 10 cities per row
        print("Minimum tour cost: {0:,}".format(round(self._value)))
        print()
        print("Total number of evaluations: {0:,}".format(self._numEval))

    def tenPerRow(self):
        for i in range(len(self._solution)):
            print("{0:>5}".format(self._solution[i]), end='')
            if i % 10 == 9:
                print()
