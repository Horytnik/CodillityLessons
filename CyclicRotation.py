def solution(A, K):
    # write your code in Python 3.6
    inpArraylenght = len(A)
    if inpArraylenght !=0:
        for i in range(0,K):
            lastNumber = A[inpArraylenght - 1]
            for i in range(inpArraylenght - 1, 0 , -1):
                A[i] = A[i-1]
            A[0] = lastNumber
    return A

print(solution([3, 8, 9, 7, 6],1))

