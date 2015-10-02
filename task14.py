n=int(input())
A=[]
B=[]
C=[0]*2
i=0
count=0
while i<n:
    C=list(map(int,input().split()))
    A.append(C[0])
    B.append(C[1])
    i+=1
    C=[]
t=int(input())
i=0
while i<n:
    if (A[i]<=t and B[i]>=t):
        count+=1
    i+=1
print(count)

