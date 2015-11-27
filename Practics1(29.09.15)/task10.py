A=list(map(int,input().split()))
t=int(input())
n=len(A)
while t>=1:
    A.insert(((len(A)-1)-A[len(A)-1]),A[len(A)-1])
    A.pop()
    t-=1
print(A)
