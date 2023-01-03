import random
import math


class Problem:
    def __init__(self):
        self._solution = None
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


# Steepest Ascent_numeric
class Numeric(Problem):
    def __init__(self):
        super().__init__() # 부모클래스 상속 
        self._expression = '' # string을 받을거란 표시
        self._domain = []
        self._delta = 0.01
    
    def setVariables(self):
    # 입력 파일을 input으로 받아서 createProblem에서 했던 것과 같은 동작을 한다.
        fileName = input('Enter the file name of a function: ')
        infile = open(fileName, 'r')
    
        lines = [line.rstrip() for line in infile]
    # 이후 self._expression, self._domain을 업데이트한다. 
        self._expression = lines[0]

        varNames = []
        low = []
        up = []

        lst = lines[1:]
        for i in lst:
            varNames.append(i.split(",")[0])
            low.append(eval(i.split(",")[1]))
            up.append(eval(i.split(",")[2]))

        self._domain = [varNames , low , up]
        print("domain :", self._domain)
        infile.close

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

        varNames = self._domain[0]

        for i in range(len(varNames)):
            exec(varNames[i] + " = " + str(current[i])) 

        valueC = eval(self._expression)
        return valueC

    def mutants(self, current):
        neighbors = []

        for i in range(len(current)):
            neighbors.append(self.mutate(current, i, self._delta ))
            # mutate도 내부 함수로 접근. self.로 받는다. 
            neighbors.append(self.mutate(current, i, -self._delta))

        return neighbors

    def mutate(self, current, i, d): ## Mutate i-th of 'current' if legal
        neighbor = current[:]
        low, up = self._domain[1], self._domain[2]

        if low[i] <= neighbor[i] + d <= up[i]:
            neighbor[i] += d
        return neighbor

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
        print(self.coordinate())  
        print("Minimum value: {0:,.3f}".format(self._value))
        print()
        super().report()

    def coordinate(self):
        c = [round(value, 3) for value in self._solution]
        return tuple(c)

# Steepest Ascent TSP
class TSP(Problem):
    def __init__(self):
        super().__init__() # 슈퍼클래스의 상속 
        self._numCities = 0
        self._locations = []
        self._distanceTable = []

    def setVariables(self):
        fileName = input('Enter the file name of a function: ')
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
        for i in range(self._numCities): # 세로 인덱스
            row = []
            for j in range(self._numCities):  # 가로 인덱스 
                dx = self._locations[i][0] - self._locations[j][0]
                dy = self._locations[i][1] - self._locations[j][1]
                d = round(math.sqrt(dx**2 + dy**2),1)
                row.append(d)
            self._distanceTable.append(row)


    def randomInit(self):      
        init = list(range(self._numCities)) # for문 사용할 필요 없다. 
        random.shuffle(init)
        return init      

    def evaluate(self, current):
        self._numEval +=1
        cost = 0
        for i in range(self._numCities-1):  # -1: 도시30개면 사이 거리는 29개만 있다. 
            cost += self._distanceTable[current[i]][current[i+1]]
        return cost


    def mutants(self, current):
        neighbors = []  # mutant 를 담는다. 
        triedPairs = []
        # inversion을 실시하기 위한 index 2개를 생성 후 inversion function call
        while len(neighbors) < self._numCities:
            i = random.randint(0, self._numCities-1)
            j = random.randint(0, self._numCities-1)
            
            # i가 작은 값이 되도록 처리한다. 
            if i > j:
                i, j = j, i
            
            # 이 때 index 2개가 중복되지 않았는지 검사하여 각기 다른 mutant가 생성되도록 실시      
            if [i,j] in triedPairs:
                continue
            else: 
                triedPairs.append([i, j])
            neighbors.append(self.inversion(current, i, j))
        return neighbors


    def inversion(self, current, i, j):
        curCopy = current[:]    
        while i < j:
            curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
            i += 1
            j -= 1
        return curCopy

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
