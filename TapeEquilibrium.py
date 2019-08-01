import sys

A = [3, 1, 2, 4, 3]

def solution(n):
    minAbs = sys.maxsize
    for a in range(0, len(n)-1):
        minAbs = min(minAbs, abs(sum(n[0:a+1]) - sum(n[a+1:len(n)])))
    return minAbs

print(solution(A))