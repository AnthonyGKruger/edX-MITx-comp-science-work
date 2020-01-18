import sys
#
sys.setrecursionlimit(1000000000)
#
# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# from math import factorial
# fac_lst = []
#
# for n in range(100):
#     fac_lst.append(factorial(n))
#
# for num in fac_lst:
#     print(str(num) + ('\n'*10))

# from math import *
#
#
# def zeros(n):
#     count = 0
#     n = [x for x in str(treefactorial(n))]
#     while n[-1] == '0':
#         n.pop()
#         count += 1
#     return count
#
#
def range_prod(lo,hi):
    if lo+1 < hi:
        mid = (hi+lo)//2
        return range_prod(lo,mid) * range_prod(mid+1,hi)
    if lo == hi:
        return lo
    return lo*hi


def treefactorial(n):
    if n < 2:
        return 1
    return range_prod(1, n)


# print(zeros(0))
# print(zeros(6))
# print(zeros(30))
# print(zeros(100000))

# def getFactorial(n):
#     """returns the factorial of n"""
#     if n == 0:
#         return 1
#     else:
#         k = n * getFactorial(n-1)
#         return k

# for k in range(1, 10000):
#     print("factorial of", k,"=", treefactorial(k))

num_lst = list(range(10000000000))

fac_lst = []

for num in num_lst:
    fac_lst.append(treefactorial(num))

print(num_lst)
print(fac_lst)