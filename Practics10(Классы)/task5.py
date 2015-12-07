__author__ = 'Егор'


class Point:
    def __init__(self, S=str()):
        for i in range(N):
            self.x, self.y = [float(j) for j in S.split(',')]

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** (0.5)


N = int(input())
x, y = 0, 0
max = 0
b1 = Point('0,0')
b2 = Point('0,0')
b3 = Point('0,0')
stor1 = 0
stor2 = 0
stor3 = 0
mastoch = [Point('0,0')] * N
a = Point(input())
mastoch[0] = a
for i in range(N - 1):
    a = Point(input())
    mastoch[i + 1] = a
for i in range(N):
    for j in range(N):
        if i != j:
            for k in range(N):
                if k != i and k != j:
                    stor1 = abs(abs(mastoch[i]) - abs(mastoch[j]))
                    stor2 = (abs(abs(mastoch[j]) - abs(mastoch[k])))
                    stor3 = (abs(abs(mastoch[i]) - abs(mastoch[k])))
                    p = (abs(abs(mastoch[i]) - abs(mastoch[j])) + abs(abs(mastoch[j]) - abs(mastoch[k])) + abs(
                        abs(mastoch[i]) - abs(mastoch[k])) / 2)
                    if (((p * (p - stor1) * (p - stor2) * (p - stor3))) ** 0.5) > max:
                        max = ((p * (p - stor1) * (p - stor2) * (p - stor3))) ** 0.5
                        b1 = mastoch[i]
                        b2 = mastoch[j]
                        b3 = mastoch[k]
print(b1.x, b1.y, ' ', b2.x, b2.y, ' ', b3.x, b3.y)