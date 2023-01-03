from setup import Setup
import random
import math

class Optimizer(Setup):
    def __init__(self):
        Setup.__init__(self)
        self._pType = 0   # Type of problem
        self._numExp = 0  # Total number of experiments

    def setVariables(self, parameters):
        Setup.setVariables(self, parameters)
        self._pType = parameters['pType']
        self._numExp = parameters['numExp']

    def getNumExp(self):
        return self._numExp

    def displayNumExp(self):
        print()
        print("Number of experiments:", self._numExp)

    def displaySetting(self):
        if self._pType == 1 and self._aType != 4 and self._aType != 6:
            print("Mutation step size:", self._delta)

class HillClimbing(Optimizer):
    def __init__(self):
        super().__init__()
        self._numRestart = 0
        self._limitStuck = 0

    def setVariables(self, parameters):
        Optimizer.setVariables(self, parameters)
        self._limitStuck = parameters['limitStuck']
        self._numRestart = parameters['numRestart']

    def displaySetting(self):
        if self._numRestart > 1:
            print("Number of random restarts:", self._numRestart)
            print()
        Optimizer.displaySetting(self)
        if 2 <= self._aType <= 3:  # First-Choice, Stochastic
            print("Max evaluations with no improvement: {0:,} iterations"
                  .format(self._limitStuck))

    def run(self,p):
        pass

    def randomRestart(self, p):          # 'alg' is the chosen hill climber
        i = 1
        self.run(p)
        bestSolution = p.getSolution()
        bestMinimum = p.getValue()   # First solution is current best
        numEval = p.getNumEval()
        while i < self._numRestart:
            self.run(p)
            newSolution = p.getSolution()
            newMinimum = p.getValue()       # New solution
            numEval += p.getNumEval()
            if newMinimum < bestMinimum:
                bestSolution = newSolution  # Update best-so-far
                bestMinimum = newMinimum
            i += 1
        p.storeResult(bestSolution, bestMinimum)

class SteepestAscent(HillClimbing):
    def displaySetting(self):
        print()
        print("Search Algorithm: Steepest Ascent")
        HillClimbing.displaySetting(self)
    
    def run(self,p):
        current = p.randomInit()
        valueC = p.evaluate(current)
        while True:
            neighbors = p.mutants(current)
            best, bestValue = self.bestOf(neighbors, p)

            if bestValue < valueC:
                current = best
                valueC = bestValue
            else:
                break
        p.storeResult(current, valueC)

    def bestOf(self, neighbors, p):
        best = neighbors[0]
        bestValue = p.evaluate(best)
        for i in range(1, len(neighbors)):
            newValue = p.evaluate(neighbors[i])
            if newValue < bestValue:
                best = neighbors[i]
                bestValue = newValue
        return best, bestValue

class FirstChoice(HillClimbing):
    def displaySetting(self):
        print()
        print("Search Algorithm: First-Choice Hill Climbing")
        HillClimbing.displaySetting(self)
        print("Max evaluations with no improvement: {0:,} iterations". format(self._limitStuck))

    def run(self, p):
        current = p.randomInit()
        valueC = p.evaluate(current)
        outfile = open('report_FirstChoice.txt', 'w')
        i = 0
        while i < self._limitStuck:
            best = p.randomMutant(current)
            bestOf = p.evaluate(best)
            if bestOf < valueC:
                current = best
                valueC = bestOf
                i = 0 
            else:
                i +=1
            outfile.write(str(round(valueC,2))+ '\n')
        outfile.close()
        p.storeResult(current, valueC)

        


class GradientDescent(HillClimbing):
    def displaySetting(self):
        print()
        print("Search Algorithm: Gradient Descent Hill Climbing")
        print()
        print("Update rate: ", self._alpha)
        print("Increment for calculating derivatives: ", self._dx)

    def run(self,p):
        currentP = p.randomInit()
        valueC = p.evaluate(currentP)
        while True:
            nextP = p.takeStep(currentP, valueC)
            valueN = p.evaluate(nextP)
            
            if valueN <= valueC:
                currentP = nextP
                valueC = valueN
            else:
                break
        p.storeResult(currentP, valueC)

class Stochastic(HillClimbing):
    def displaySetting(self):
        print()
        print("Search Algorithm: Stochastic Hill Climbing")
        print()
        HillClimbing.displaySetting(self)

    def run(self,p):
        current = p.randomInit()
        valueC = p.evaluate(current)
        i = 0
        while i <self._limitStuck:
            neighbors = p.mutants(current)
            best, bestValue = self.stochasticBest(neighbors, p)
            if bestValue < valueC:
                current = best
                valueC = bestValue
                i = 0
            else:
                i += 1
        p.storeResult(current, valueC)

    def stochasticBest(self, neighbors, p):
        valuesForMin = [p.evaluate(indiv) for indiv in neighbors]
        largeValue = max(valuesForMin) + 1
        valuesForMax = [largeValue - val for val in valuesForMin]

        total = sum(valuesForMax)
        randValue = random.uniform(0,total)
        s = valuesForMax[0]
        for i in range(len(valuesForMax)):
            if randValue <= s: 
                break
            else:
                s += valuesForMax[i+1]
        return neighbors[i], valuesForMin[i]
        

class MetaHeuristics(Optimizer):
    def __init__(self):
        Optimizer.__init__(self)
        self._limitEval = 0     # Total # evaluations until temination
        self._whenBestFound = 0 # This is actually a result of experiment

    def setVariables(self, parameters):
        Optimizer.setVariables(self, parameters)
        self._limitEval = parameters['limitEval']

    def getWhenBestFound(self):
        return self._whenBestFound

    def displaySetting(self):
        Optimizer.displaySetting(self)
        print("Number of evaluations until termination: {0:,}"
              .format(self._limitEval))

    def run(self):
        pass


class SimulatedAnnealing(MetaHeuristics):
    def __init__(self):
        MetaHeuristics.__init__(self)
        self._numSample = 100  # Number of samples used to determine 
                               #  initial temperature
    def displaySetting(self):
        print()
        print("Search Algorithm: Simulated Annealing")
        print()
        MetaHeuristics.displaySetting(self)

    def run(self, p):
        current = p.randomInit()
        valueC = p.evaluate(current)
        best, valueBest = current, valueC
        whenBestFound = i = 1  # To remember when best was found
        t = self.initTemp(p)   # An initial temperature is chosen
        outfile = open('report_simulatedAnnealing.txt', 'w')
        while True:
            t = self.tSchedule(t)   # Follow annealing schedule
            if t == 0 or i == self._limitEval:
                break
            neighbor = p.randomMutant(current)
            valueN = p.evaluate(neighbor)
            i += 1
            dE = valueN - valueC
            if dE < 0:
                current = neighbor
                valueC = valueN
            elif random.uniform(0, 1) < math.exp(-dE/t):
                current = neighbor  # Move to a worse neighbor
                valueC = valueN
            if valueC < valueBest:  # A new best solution found
                (best, valueBest) = (current, valueC)
                whenBestFound = i   # Record when best was found
                outfile.write(str(round(valueBest,2)) + '\n')
        self._whenBestFound = whenBestFound
        outfile.close()
        p.storeResult(best, valueBest)

    def initTemp(self, p): # To set initial acceptance probability to 0.5
        diffs = []
        for i in range(self._numSample):
            c0 = p.randomInit()     # A random point
            v0 = p.evaluate(c0)     # Its value
            c1 = p.randomMutant(c0) # A mutant
            v1 = p.evaluate(c1)     # Its value
            diffs.append(abs(v1 - v0))
        dE = sum(diffs) / self._numSample  # Average value difference
        t = dE / math.log(2)        # exp(–dE/t) = 0.5
        return t

    def tSchedule(self, t):
        return t * (1 - (1 / 10**4))

