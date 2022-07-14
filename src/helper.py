from itertools import combinations
def powerset(array):
    result = []
    n = len(array)
    for i in range(n,0,-1):
        for element in combinations(array,i):
            result.append(' '.join(element))
    return result

def intersection(array1, array2):
    result = []
    for element in array1:
        if element in array2:
            result.append(element)
    return result

def unique(array1):
    result = []
    for element in array1:
        if element not in result:
            result.append(element)
    return result