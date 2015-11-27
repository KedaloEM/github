n=int(input())
N = list(map(int, input().split()))
sred=sum(N)/n
i=0
minr=abs(N[i]-sred)
while i<n:
    if abs(N[i]-sred)<minr:
        minr=abs(N[i]-sred)
        b=N[i]
    i+=1        
print(b)




