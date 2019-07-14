def solution(A):
    notPaired = 0
    for value in A:
        notPaired = value ^ notPaired # xor of all elements leads to odd element
    return notPaired
