# from sa_problem_skeleton_classVer import Numeric
from sa_problem_skeleton_classVer import TSP


def main():
    # Numeric class function 생성
    # cls = Numeric()
    cls = TSP()

    # serVariable을 이용해 문제 읽어오기
    cls.setVariables()

    # steepestAscent 실행
    steepestAscent(cls)

    # describe, report를 이용해 결과 도출
    cls.describe()
    cls.report()


def steepestAscent(cls):
    # Random한 초기값을 생성
    current = cls.randomInit()
    # 초기값에 대한 함수값을 계산
    valueC = cls.evaluate(current)
    # 계산을 반복하며 mutant를 생성후 더 나은 solution을 탐색
    while True:
        # mutant를 생성
        neighbors = cls.mutants(current)   

        # mutant 중 가장 좋은 solution을 선택
        # 각각의 neighbor에 대해서 함수 값을 계산해 보고,
        # 현재 값 보다 좋은 것이 있으면 거기로 이동한다.
        best, bestValue = bestOf(neighbors, cls) 

        # best solution 업데이트
        if bestValue >= valueC:
            break
        else:
            current = best
            valueC = bestValue
        print(valueC)
    # Best solution과 그때의 Cost를 반환
    cls.storeResult(current, valueC)


def bestOf(neighbors, cls):
    # neighbors 각각에 대한 evaluation을 실시하여
    # 가장 좋은 solution을 best로 선정 후 반환

    # 1. 제일 처음 sample을 best라고 가정한다.
    best = neighbors[0] 
    bestValue = cls.evaluate(best)

    # 2. 두 번째 부터 계속 비교하면서, 더 좋은게 찾아지면 best로 저장해둔다.
    for i in range(1, len(neighbors)):
        newValue = cls.evaluate(neighbors[i])
        if newValue < bestValue:
            best = neighbors[i]
            bestValue = newValue

    # 3. 비교가 모두 끝나면 best를 반환한다.
    return best, bestValue


def displaySetting(cls):
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", cls.getDelta())


main()