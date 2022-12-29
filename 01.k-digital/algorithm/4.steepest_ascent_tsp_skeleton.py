import random
import math

NumEval = 0    # Total number of evaluations

def main():
    # Create an instance of numerical optimization problem
    # 입력 txt 파일에서 수식과 변수의 범위를 읽어와 반환  
    p = createProblem()   # 'p': (numcities, location, table)
    
    # Call the search algorithm
    # SteepestAscent 알고리즘을 실행하여 solution을 구하기
    solution, minimum = steepestAscent(p) 

    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()

    # Report results
    displayResult(solution, minimum)

def createProblem(): ###
    ## Read in a TSP (# of cities, locatioins) from a file.
    ## Then, create a problem instance and return it.
    # txt 파일 이름을 입력 받아서 open 한다.
    fileName = input('Enter the file name of a TSP: ')
    infile = open(fileName, 'r')
    
    # First line is number of cities
    # 첫 번째 줄에는 도시의 수가 기록되어 있음
    numCities = int(infile.readline())

    # 두 번째 줄 부터는 각 도시의 위치 (x, y 좌표) 가 기록되어 있음
    locations = []    
    line = infile.readline()
    while line != '':
        locations.append(eval(line))
        line = infile.readline()

    infile.close()  

    # 각 도시 사이의 거리를 미리 계산해 둠 (추후 계산의 편의를 위해)
    table = calcDistanceTable(numCities, locations)
    return numCities, locations, table


def calcDistanceTable(numCities, locations):
    # 도시 사이의 거리를 미리 계산해 두어서 표로 준비
    # 직선 거리는 아래와 같은 수식을 이용해 구한다
    # dist = sqrt((x1-x2)^2 + (y1-y2)^2)
    table = []
    for i in range(numCities): # 세로 인덱스
        row = []
        for j in range(numCities):  # 가로 인덱스 
            dx = locations[i][0] - locations[j][0]
            dy = locations[i][1] - locations[j][1]
            d = round(math.sqrt(dx**2 + dy**2),1)
            row.append(d)
        table.append(row)
    # 출력 예시
    # table: [[0.0, 80.4487, 46.0997, ...], [80.4487, 0.0, 47.1699, ...], ...]
    # 이중 list 이고, table[i][j] 의 값은 i번쨰 도시와 j번째 도시 사이의 직선 거리를 나타냄
    return table # A symmetric matix of pairwise distances 


def steepestAscent(p):
    # 시작 지점으로 Random한 방문 순서를 생성
    current = randomInit(p)

    # 생성한 시작 지점의 방문 비용을 evaluate로 계산
    valueC = evaluate(current, p)
    # 계산을 반복하며 mutant를 생성후 더 나은 solution을 탐색
    while True:
        # mutant를 생성
        neighbors = mutants(current, p)   

        best, bestValue = bestOf(neighbors, p) 

        # best가 현재보다 좋으면 업데이트, 아니면 break
        if bestValue >= valueC:
            break
        else:
            current = best
            valueC = bestValue
        print(valueC)
    # Best solution과 그때의 Cost를 반환
    return current, valueC


def randomInit(p):
    # Return a random initial tour
    # 도시의 index를 이용해 방문 순서를 정할 것이므로,
    # random한 index 순서로 생성
    # 예를들어 도시가 30개 있을 경우,
    # [5, 2, 0, 29, ..., 1] 과 같이 index의 중복이 없이 랜덤한 순서를 만든다.

    numCities = p[0]
    init = list(range(numCities)) # for문 사용할 필요 없다. 
    # print("init:", init)
    random.shuffle(init)
    # print("randomInit:", init, "lenth:", len(init))
    return init


def evaluate(current, p):
    global NumEval
    NumEval +=1
    ## Calculate the tour cost of 'current'
    ## 'p' is a Problem instance
    ## 'current' is a list of city ids
    # TSP의 비용은 총 이동한 거리의 합으로 계산한다.
    # distanceTable은 p[2]에서 제공됨
    table = p[2]
    numCities = p[0]
    # cost = (0번째 도시~1번째 도시 거리) + (1번째 도시~2번째 도시 거리) + ...
    cost = 0
    for i in range(numCities-1):  # -1: 도시30개면 사이 거리는 29개만 있다. 
        cost += table[current[i]][current[i+1]]
    return cost


def mutants(current, p):
    # Apply inversion
    # inversion을 이용해 여러개의 mutant를 생성한다.
    # mutant는 도시의 수 만큼 생성하기로 하자.
    numCities = p[0]
    print("numCities length:", numCities)
    neighbors = []  # mutant 를 담는다. 

    triedPairs = []
    # inversion을 실시하기 위한 index 2개를 생성 후 inversion function call
    while len(neighbors) < numCities:
        i = random.randint(0, numCities-1)
        j = random.randint(0, numCities-1)
        
        # i가 작은 값이 되도록 처리한다. 
        if i > j:
            i, j = j, i

        # 이 때 index 2개가 중복되지 않았는지 검사하여 각기 다른 mutant가 생성되도록 실시      
        if [i,j] in triedPairs:
            continue
        else: 
            triedPairs.append([i,j])

        neighbors.append(inversion(current, i, j))

    # hint: triedPairs = [] 라는 list를 만들어서, [i, j]가 생성된 것을 저장 후
    # 새로 만든 [i, j] 가 이미 생성되었는지 아래 expression을 이용해 확인 가능
    # if [i, j] in triedPairs
    return neighbors


def inversion(current, i, j): ## Perform inversion
    curCopy = current[:]    
    while i < j:
        curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
        i += 1
        j -= 1

    # 예시
    # current: [1, 2, 3, 4, 5]
    # i: 1, j:3
    # curCopy: [1, 4, 3, 2, 5]
    return curCopy


def bestOf(neighbors, p):
    # neighbots 중 가장 cost가 작은 neighbor 선정
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
    n = p[0]
    print("Number of cities:", n)
    print("City locations:")
    locations = p[1]
    for i in range(n):
        print("{0:>12}".format(str(locations[i])), end = '')
        if i % 5 == 4:
            print()

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")

def displayResult(solution, minimum):
    print()
    print("Best order of visits:")
    tenPerRow(solution)       # Print 10 cities per row
    print("Minimum tour cost: {0:,}".format(round(minimum)))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def tenPerRow(solution):
    for i in range(len(solution)):
        print("{0:>5}".format(solution[i]), end='')
        if i % 10 == 9:
            print()

main()
