InpArray = [1,3,1,4,2,3,5,4]
Pos = 5

def solution(X,A):
    maxInd = 0
    if len(set(A)) == X:
        for SetElm in set(A):
            maxInd = max(maxInd, A.index(SetElm))
        return maxInd
    else:
        return -1



print(solution(Pos, InpArray))

print(solution(2, [2, 2, 2, 2, 2]))

print(solution(3, [1, 3, 1, 3, 2, 1, 3]))

