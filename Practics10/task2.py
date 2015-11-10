__author__ = 'student'
class Point:
    def __init__(self, S = str()):
        for i in range(N):
            self.x, self.y = [float(j) for j in S.split(',')]
    def __abs__(self):
        return(self.x **2 + self.y**2)**(0.5)
N=int(input())
max=0
x,y=0,0
for i in range(N):
    a=Point(input())
    if abs(a)>max:
        max=abs(a)
        x=a.x
        y=a.y
print(x,y)
