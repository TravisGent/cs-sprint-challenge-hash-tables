def has_negatives(a):
    result = []

    newDict = {}
    for item in a:
        newDict[str(item)] = item

    for item in a:
        if "-" + str(item) in newDict:
            result.append(item)

    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
