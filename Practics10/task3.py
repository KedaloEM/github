__author__ = 'student'
class Point:
    def __init__(self, S = str()):
        for i in range(N):
            self.x, self.y = [float(j) for j in S.split(',')]
    def __abs__(self):
        return(self.x **2 + self.y**2)**(0.5)
N=int(input())
x,y=0,0
a=Point(input())
x=a.x
y=a.y
for i in range(N-1):
    a=Point(input())
    x=(x+a.x)/2
    y=(x+a.y)/2
print(x,y)