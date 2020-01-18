def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    return_list = []
    count = 0
    for char in s:
        if char in num_list:
            count += 1
            return_list.append(int(char))
    if count > 0:
        return sum(return_list)
    else:
        raise ValueError

print(sum_digits("a;d"))