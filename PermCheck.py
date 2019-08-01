A = [2,3,1,5]
B = [2,3,1,4]
C = [1, 4, 1]

def allElmSum(n):
    sum = 0
    for a in range(1,n+1):
        sum = sum + a
    return sum

def solution(inp):
    ArrayElementSum =  sum(set(inp))
    ArrayCountSum  = allElmSum(len(inp))
    if ArrayElementSum == ArrayCountSum:
        return 1
    else:
        return 0

print(solution(A))

print(solution(B))

print(solution(C))

