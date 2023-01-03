from optimizer import *
from problem import * 

def main():
    # Problem 오브젝트 생성 후 선택
    p, pType = selectProblem()
    # 알고리즘 선택
    alg = selectAlgorithm(pType)
    # search 알고리즘 선택
    alg.run(p)

    p.describe()

    alg.displaySetting()

    p.report()


def selectProblem():
    print("Select the problem type:")
    print("  1.  Numerical Optimization")
    print("  2.  TSP")
    pType = int(input("Enter the number: "))
    if pType == 1:
        p = Numeric()
    elif pType == 2:
        p = Tsp()
    p.setVariables()
    return p, pType

def selectAlgorithm(pType):
    print()
    print("Select the search algorithm:")
    print("  1. Steepest-Ascent")
    print("  2. First-Choice")
    print("  3. Gradient Descent")
    print("  4. Stochastic Gradient Descent")
    while True:
        aType = int(input("Enter the number:  "))
        if not invalid(pType, aType):
            break
    optimizers = { 1: 'SteepestAscent()',
                   2: 'FirstChoice()',
                   3: 'GradientDescent()',
                   4: 'Stochastic()'  }
    alg = eval(optimizers[aType])
    alg.setVariables(pType)
    return alg

def invalid(pType, aType):
    if pType == 2 and aType == 3:
        print("You cannot choose Gradient Descent")
        print("    unless you want a function")
        return True
    else:
        return False

main()    

