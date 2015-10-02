A=list(map(int,input().split()))
summ=0
i=0
kolvodvoy=0
while i<=9:
    if i<9:
        if  A[i]==2 and A[i+1]!=2:
            summ+=A[i+1]
            i+=1
            kolvodvoy+=1
        else:
            summ+=A[i]
    else:
        summ+=A[i]
    i+=1
print((summ/(10-kolvodvoy))//1)
