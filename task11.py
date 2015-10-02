k=int(input())
n=int(input())
A=[0]*(n+2)
i=0
while i<=n:
    if i<=k-1:
        A[i]=1
    else:
        A[i]=sum(A[i-k:i])
    i+=1
print(A[n])

