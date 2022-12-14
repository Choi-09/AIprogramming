import random
import math
import time

DELTA = 0.01   # Mutation step size
LIMIT_STUCK = 100 # Max number of evaluations enduring no imp..? 
NumEval = 0    # Total number of evaluations


def main():
    # Create an instance of numerical optimization problem
    # 입력 txt 파일에서 수식과 변수의 범위를 읽어와 반환  
    p = createProblem()   # 'p': (expr, domain)
    # print("p:", p)
    # Call the search algorithm
    # SteepestAscent 알고리즘을 실행하여 solution을 구하기
    solution, minimum = firstChoice(p) # 주변에서 가장 좋은곳으로 이동한다. 

    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()

    # Report results
    displayResult(solution, minimum)

def createProblem(): ###
    ## Read in an expression and its domain from a file.
    ## Then, return a problem 'p'.
    ## 'p' is a tuple of 'expression' and 'domain'.
    ## 'expression' is a string.        
    ## 'expression'은 txt 파일의 첫 줄에 있는 수식 string
    ## 'domain' is a list of 'varNames', 'low', and 'up'.
    ## txt 파일의 두 번째 줄 부터는 변수명,최소값,최대값
    ## 'varNames' is a list of variable names.
    ## 'varNames'는 각 변수의 이름이 저장 됨
    ## 'low' is a list of lower bounds of the varaibles.
    ## 'low'에는 각 변수의 최소값이 저장됨
    ## 'up' is a list of upper bounds of the varaibles.
    ## 'up'에는 각 변수의 최대값이 저장됨
    # input function을 이용해 읽어올 txt 파일의 경로를 얻어옴
    # readline()을 이용해 각 줄의 정보를 읽어옴

    fileName = input('파일 이름을 입력하세요')
    infile = open(fileName, 'r')
   
    lines = [line.rstrip() for line in infile]
    
    expression = lines[0]
    # print("expression: ", expression)
    
    varNames = []
    low = []
    up = []

    lst = lines[1:]
    for i in lst:
        varNames.append(i.split(",")[0])
        low.append(eval(i.split(",")[1]))
        up.append(eval(i.split(",")[2]))


    domain = [varNames , low , up]
    print("domain :", domain)
    infile.close
    return expression, domain


def firstChoice(p):
    # Random한 초기값을 생성
    current = randomInit(p)
    # 초기값에 대한 함수값을 계산
    valueC = evaluate(current, p)
    # 계산을 반복하며 mutant를 생성후 더 나은 solution을 탐색
    i = 0
    while i < LIMIT_STUCK:
        best = randomMutant(current, p)
        bestOf = evaluate(best,  p)
        if bestOf < valueC:
            current = best
            valueC = bestOf
            i = 0 
        else:
            i +=1
        print(i)
    return current, valueC


def randomInit(p):
    # Return a random initial point
    # as a list of values
    # 초기 값을 만들기 위해 랜덤한 값들을 만들기

    # domain의 low, up 정보를 이용해
    # low <= value <= up 범위에 해당하는 값을 random.uniform을 통해 생성
    # list 형태로 각 변수의 초기 값을 반환
    domain = p[1]
    low, up = domain[1], domain[2]
    init = []
    for i in range(len(low)):
        init.append(random.uniform(low[i], up[i]))
    
    return init


def evaluate(current, p):
    ## Evaluate the expression of 'p' after assigning
    ## the values of 'current' to the variables

    # Number of evaluation을 기록하기 위해 global 변수 이용
    global NumEval
    NumEval += 1

    # expression과 variable name을 읽어오고
    # 이를 이용해 x=value 형태의 string을 만든 뒤,
    # exec 를 이용해 실제로 실행하여 값을 할당 후
    domain = p[1]  
    varNames = domain[0]

    for i in range(len(varNames)):
        exec(varNames[i] + " = " + str(current[i])) 
        # str은 계산안되니까 실행만 하면됨.

    # expression에 eval을 이용해 함수 값을 계산
    expression = p[0]
    valueC = eval(expression)
    # print(valueC)

    # 함수를 current를 이용해서 계산했을 때의 값
    return valueC

def mutants(current):
    neighbors = []
    for i in range(len(current)):  # For each variable
        mutant = mutate(current, i, DELTA)
        neighbors.append(mutant)
        mutant = mutate(current, i, -DELTA)
        neighbors.append(mutant)
    return neighbors

def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal

    # 현재 값에대한 복사본을 slicing을 이용해 생성
    neighbor = current[:]  # logical errer 주의! 

    # 복사 된 값에 mutation을 실시하며, 이 때 domain 정보를 이용해
    # low <= value <= up 사이의 유효한 값이 얻어지도록 확인
    domain = p[1]
    low, up = domain[1], domain[2]

    if low[i] <= neighbor[i] + d <= up[i]:
        neighbor[i] += d

    # neighbor: 값이 5개 들어있는 list(current와 동일한 형태)
    return neighbor


def randomMutant(current, p):
    # pick a random locus
    i = random.randint(0,len(current)-1)
    
    # Mutate the chosen locus
    if random.uniform(0,1) > 0.5:
        d = DELTA
    else:
        d = -DELTA

    return mutate(current, i, d, p)


def bestOf(neighbors, p):
    # neighbors 각각에 대한 evaluation을 실시하여
    # 가장 좋은 solution을 best로 선정 후 반환

    # 1. 제일 처음 sample을 best라고 가정한다.
    best = neighbors[0] 
    bestValue = evaluate(best, p)

    # 2. 두 번째 부터 계속 비교하면서, 더 좋은게 찾아지면 best로 저장해둔다.
    for i in range(1, len(neighbors)):
        newValue = evaluate(neighbors[i], p)
        if newValue < bestValue:
            best = neighbors[i]
            bestValue = newValue

    # 3. 비교가 모두 끝나면 best를 반환한다.
    return best, bestValue


def describeProblem(p):
    print()
    print("Objective function:")
    # expression 출력
    print(p[0])   # Expression
    print("Search space:")
    # Domain 정보 출력
    varNames = p[1][0] # p[1] is domain: [VarNames, low, up]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(" " + varNames[i] + ":", (low[i], up[i])) 

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

def displayResult(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))  # Convert list to tuple
    print("Minimum value: {0:,.3f}".format(minimum))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)  # Convert the list to a tuple


main()
