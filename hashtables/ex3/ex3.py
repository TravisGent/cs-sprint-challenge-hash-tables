def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []
    newDictionaryArray = []
    i = 0
    while i < len(arrays):
        newDict = {}
        for item in arrays[i]:
            newKey = str(item)
            newDict[newKey] = item
        newDictionaryArray.append(newDict)
        i += 1

    for item in arrays[0]:
        y = 0
        counter = 0
        while y < len(newDictionaryArray):
            if str(item) in newDictionaryArray[y]:
                counter += 1
            y +=1
        if (counter == len(arrays)):
            result.append(item)

    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))