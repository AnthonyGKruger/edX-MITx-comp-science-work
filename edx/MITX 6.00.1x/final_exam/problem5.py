
def f(a, b):

    return a > b




def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    interdiff = {}
    difference_dict = {}
    for k, v in d2.items():
        if k not in d1.keys():
            difference_dict[k] = v
    for k, v in d1.items():
        if k not in d2.keys():
            difference_dict[k] = v
    for k, v in d1.items():
        if k in d2.keys():
            interdiff[k] = f(d1[k], d2[k])
    return interdiff, difference_dict



print(dict_interdiff({1: 30, 2: 20, 3: 30}, {1: 40, 2: 50, 3: 60}))





















    # If
    # f(a, b)
    # returns
    # a + b
    # d1 = {1: 30, 2: 20, 3: 30, 5: 80}
    # d2 = {1: 40, 2: 50, 3: 60, 4: 70, 6: 90}
    # then
    # dict_interdiff(d1, d2)
    # returns({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})

    # If
    # f(a, b)
    # returns
    # a > b
    # d1 = {1: 30, 2: 20, 3: 30}
    # d2 = {1: 40, 2: 50, 3: 60}
    # then
    # dict_interdiff(d1, d2)
    # returns({1: False, 2: False, 3: False}, {})
    #
