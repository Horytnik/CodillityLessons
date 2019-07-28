A = [3, 1, 2, 4, 3]

def solution(n):
    print(n)
    SortedArray = sorted(n)
    oldAbsDiff = 100000
    for a in range(0, len(SortedArray)-1):
        FirstSum = sum(SortedArray[0:a+1])
        SecondSum = sum(SortedArray[a+1:len(SortedArray)])
        newAbsDiff = abs(FirstSum - SecondSum)
        if newAbsDiff < oldAbsDiff:
            minAbs = newAbsDiff
        oldAbsDiff = abs(FirstSum - SecondSum)
    return minAbs

print(solution(A))