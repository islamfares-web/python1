class Vectors(list):
    def __init__(self, other):
        assert len(other) != 0, "Invalid Input!"
        for e in other:
            assert type(e) == int or type(e) == float, "Invalid Input!"
        list.__init__(self, other)

    def __str__(self):

        s = " "
        for x in self:
            s += str(x) + ','
        return '<' + s[:-1] + ' >'

    def __add__(self, other):
        assert len(self) == len(other), 'Invalid Input!'
        L = []
        for x in range(len(self)):
            L.append(self[x] + other[x])
        return Vectors(L)

    def __sub__(self, other):
        assert len(self) == len(other), 'Invalid Input!'
        L = []
        for x in range(len(self)):
            L.append(self[x] - other[x])
        return Vectors(L)

    def __mul__(self, other):
        assert len(self) == len(other), 'Invalid Input!'
        L = []
        for x in range(len(self)):
            L.append(self[x] * other[x])

        dotproduct = 0
        for x in L:
            dotproduct += x
        return dotproduct

    def norm(self):
        assert len(self) != 0, 'Invalid Input!'
        norm = 0
        for x in self:
            norm += x ** 2
        return norm ** 0.5

    def __neg__(self):
        Vector = []
        for x in self:
            Vector.append(-x)

        return Vectors(Vector)


def zeros(n):
    return Vectors([0] * n)


def ones(n):
    return Vectors([1] * n)


import copy

v = Vectors([1, 2.3])
w = zeros(5)
u = ones(2)
print(v)
print(w)
print(v[1])
print(v + v + v)
print(v * u)
print(v.norm())
w[2] = 3.5
v = copy.deepcopy(w)
print(v)
print(-v)
w[0] = 15.5
w[4] = -12
print(w - v)
print(-w + v)