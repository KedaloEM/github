__author__ = 'student'
class Point:
    def __init__(self, S):
        self.x, self.y = [float(i) for i in S.split(',')]
    def __add__(self, other):
        S_new =str(self.x + other.x)+','+str(self.y + other.y)
        return Point(S_new)
    def __sub__(self, other):
        S_new =str(self.x - other.x)+','+str(self.y - other.y)
        return Point(S_new)
    def __mul__(self, other):
        S_new =str(self.x * other.x)+','+str(self.y * other.y)
        return Point(S_new)
    def __truediv__(self, other):
        S_new =str(self.x / other.x)+','+str(self.y / other.y)
        return Point(S_new)
    def __str__(self):
        return str(self.x) +','+ str(self.y)
a=Point(input())
b=Point(input())
print(a.__add__(b))


