def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    # Your code here
    odd_list = []
    for num in L:
        if L.count(num) % 2 != 0:
            odd_list.append(num)
    if odd_list == []:
        return None
    else:
        return max(odd_list)


print(largest_odd_times([2,2,4,4]))
print(largest_odd_times([3,9,5,3,5,3]))

