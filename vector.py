class Vector:

    def __init__(self, *nums):
        self.storage = nums
        self.dim = len(self.storage)

    def __add__(self, other):
        temp = [self.storage[i] + other.storage[i] for i in range(self.dim)]
        return Vector(*temp)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return float(sum([a_i*b_i for a_i, b_i in zip(self.storage, other.storage)]))
        else:
            nums = [n * other for n in self.storage]
            return Vector(*nums)

    def norm(self):
        return (self * self) ** 0.5

    def __str__(self):
        return "Vector: {}".format(self.storage)

    def __repr__(self):
        return self.__str__()