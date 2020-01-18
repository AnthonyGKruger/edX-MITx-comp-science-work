class myDict(object):
    """ Implements a dictionary without using a dictionary """

    def __init__(self):
        """ initialization of your representation """
        # FILL THIS IN
        self.frame = {}

    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        # FILL THIS IN
        self.frame[k] = v

    def getval(self, k):
        """ k, immutable object  """
        if k in self.frame.keys():
            return self.frame[k]
        else:
            raise KeyError

    def delete(self, k):
        """ k, immutable object """
        # FILL THIS IN
        if k in self.frame.keys():
            self.frame.pop(k)
        else:
            raise KeyError


# With a dict:  |    With a myDict:
# -------------------------------------------------------------------------------
# d = {}             md = myDict()        # initialize a new object using
#                                           your choice of implementation
#
# d[1] = 2           md.assign(1,2)       # use assign method to add a key,value pair
#
# print(d[1])        print(md.getval(1))  # use getval method to get value stored for key 1
#
# del(d[1])          md.delete(1)         # use delete method to remove
#                                           key,value pair associated with key 1