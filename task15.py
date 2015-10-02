n=int(input())
A = list(map(int, input().split()))
B=[0]*n
k=int(input())
s=0
i=0
while i<n-k:
    j=0
    while j<k:
        B[i]=B[i]+A[i+j]
        j+=1
    i+=1
print(max(B))
