class Point(object):
    def __init__(self, x=0, y=0):
        assert (type(x) == int or type(x) == float) and (type(y) == int or type(y) == float), "Bad input!"
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


class Rectangle(object):

    def __init__(self, p, q):
        assert type(p) == Point and type(q) == Point and p.x <= q.x and p.y <= q.y, 'Bad Input!'
        self.p = p
        self.q = q

    def __str__(self):
        return '"(p= ' + str(self.p) + ', q= ' + str(self.q) + ')"'

    def height(self):
        height = self.q.y - self.p.y
        return height

    def width(self):
        width = self.q.x - self.p.x
        return width

    def perimeter(self):
        perimeter = self.width() * 2 + self.height() * 2

        return perimeter

    def Area(self):
        Area = self.width() * self.height()

        return Area

    def contains(self,item):
        assert type(item)==Point,'Bad Input!'
        if item.x<=self.q.x and item.x>=self.p.x and item.y<=self.q.y and item.y>=self.p.y:
            return True
        return False


p = Point(1, 2)
q = Point(3.2, 4)
R = Rectangle(p, q)
print(R)
print(R.width())
print(R.height())
print(R.Area())
print(R.perimeter())
print(R.contains(Point(1.5, 3)))
print(R.contains(Point(10.5, 3)))