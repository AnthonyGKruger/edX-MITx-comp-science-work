def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    exponent = 0
    total = base ** exponent
    while True:
        if total == num and exponent > 0:
            exponent -= 1
            break
        elif total == num and exponent == 0:
            break
        if num == 1:
            break
        if total < num:
            exponent += 1
            total = base ** exponent
            test_case = (base**(exponent - 1))
            continue
        if abs(test_case - num) < abs(total - num):
            exponent -= 1
            break
        elif abs(test_case - num) == abs(total - num):
            exponent -= 1
            break
        else:
            break
    return exponent


print(closest_power(2, 1))
