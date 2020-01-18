def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    mul_list = []
    for i in range(len(listA)):
        mul_list.append(listA[i] * listB[i])
    return sum(mul_list)

listA = [1, 2, 3]
listB = [4, 5, 6]

print(dotProduct(listA,listB))
