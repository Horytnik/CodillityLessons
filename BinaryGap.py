def Solution(N):
    zeroCounter = 0
    allZerosCountedList = []
    binValue = bin(N)
    stringValue = str(binValue)

    for i in range(2, len(stringValue)):
        if int(stringValue[i]) == 0:
            zeroCounter = zeroCounter + 1 # count amount of zeros
        if int(stringValue[i]) == 1:
            allZerosCountedList.append(zeroCounter) # count till 1
            zeroCounter = 0

    result = max(allZerosCountedList)
    return result