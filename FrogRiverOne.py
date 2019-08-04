InpArray = [1,3,1,4,2,3,5,4]
Pos = 5

def solution(X,A):
    if len(set(A)) == X:
        leafpositions = [0]*X
        amountoffields = X
        for index in range(0, len(A)):
            if leafpositions[A[index]-1] == 0:
                leafpositions[A[index]-1] = 1
                amountoffields -= 1
                if amountoffields == 0:
                    return index
    else:
        return -1

print(solution(Pos, InpArray))

print(solution(2, [2, 2, 2, 2, 2]))

print(solution(3, [1, 3, 1, 3, 2, 1, 3]))

