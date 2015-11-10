__author__ = 'student'
class Point:
    def __init__(self, S = str()):
        for i in range(N):
            self.x, self.y = [float(j) for j in S.split(',')]
    def __abs__(self):
        return(self.x **2 + self.y**2)**(0.5)
N=int(input())
x,y=0,0
max=0
max1=0
max2=0
a=Point(input())
a1=a
x=a.x
y=a.y
for i in range(N-1):
    a=Point(input())
    if abs(a1-a)>max:


print(x,y)