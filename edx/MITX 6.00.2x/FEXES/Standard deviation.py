L = ['apples', 'oranges', 'kiwis', 'pineapples']

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if L == []:
        return float('NaN')
    else:
        mean = (sum([len(str(t)) for t in L])) / len(L)
        return round((sum([(len(str(t))-mean)**2 for t in L]) / len(L)) ** 0.5, 3)

# def stdDevOfLengths1(L):
#     n = len(L)
#     if (n == 0):
#         return float('NaN')
#     lengths    = [len(s) for s in L]
#     mean       = sum(lengths) / n
#     squaredDev = [(l-mean)**2 for l in lengths]
#     variance   = sum(squaredDev) / n
#     return variance**(.5)

print(stdDevOfLengths([10, 4, 12, 15, 20, 5]))
# print(stdDevOfLengths1(L))