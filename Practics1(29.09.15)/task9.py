A=[1,4,6,7,9,3,2,50,6,3,4,47,67]
for i in range((len(A)//2)+1):
    if A[i]==A[len(A)-i-1]:
        print(A[i])
        break
    print(A[i],'',A[len(A)-i-1],end='  ')
    
