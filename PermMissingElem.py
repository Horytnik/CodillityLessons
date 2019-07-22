A = [2,3,1,5]
B = []
C = [1]
D = [2,1,3,4,5,7]
E = [2,1,3,4,5,6]
F = [2,7,3,4,5,6]
G = [1,2]

def allElmSum(n):
    sum = 0
    for a in range(1,n+1):
        sum = sum + a
    return sum


def solution(A):
    ElementsSum = sum(A)
    SumOfArray = allElmSum(len(A)+1)
    return (SumOfArray - ElementsSum)


print('Sol',solution(A))
print('Sol',solution(B))
print('Sol',solution(C))
print('Sol',solution(D))
print('Sol',solution(E))
print('Sol',solution(F))
print('Sol',solution(G))