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


class Numeric(Problem):
    def __init__(self):
        super().__init__() # 부모클래스 상속 
        self._expression = '' # string을 받을거란 표시
        self._domain = []
        self._delta = 0.01
    
    def setVariables(self):
    # 입력 파일을 input으로 받아서 createProblem에서 했던 것과 같은 동작을 한다.
        fileName = input('파일 이름을 입력하세요')
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
