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
b1=Point('0,0')
b2=Point('0,0')
b3=Point('0,0')
mastoch=[Point('0,0')]*N
a = Point(input())
mastoch[0]=a
for i in range(N-1):
    a =Point(input())
    mastoch[i+1]=a
for i in range(N):
    for j in range(N):
        if i!=j:
            for k in range(N):
                if k!=i and k!=j:
                    if (abs(abs(mastoch[i])-abs(mastoch[j])) + abs(abs(mastoch[j])-abs(mastoch[k]))+abs(abs(mastoch[i])-abs(mastoch[k])))>max:
                        max=abs(abs(mastoch[i])-abs(mastoch[j])) + abs(abs(mastoch[j])-abs(mastoch[k]))+abs(abs(mastoch[i])-abs(mastoch[k]))
                        b1=mastoch[i]
                        b2=mastoch[j]
                        b3=mastoch[k]
print(b1.x,b1.y,' ',b2.x,b2.y,' ',b3.x,b3.y)
