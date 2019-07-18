def solution(X, Y, D):
    result = round((Y-X)/D)
    if (result*D+X) < Y:
        result = result + 1
    if X == Y:
        result = 0
    return result

print(solution(10,85,30)) #expected 3
print(solution(1, 5, 2)) #expected 2
