A = [2,3,1,5]

def Factorial(FacNum):
    if FacNum == 0:
        return 1
    else:
        return FacNum + Factorial(FacNum-1)

def solution(A):
    ElementsSum = sum(A)
    SumOfArray = Factorial(len(A))
    return (ElementsSum - SumOfArray - 1)

print(solution(A))


print(Factorial(len(A)))