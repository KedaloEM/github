A=[1,2,3,5,3,7,9,13]
B=A
C=A
for elem in A:
    if A.count(elem)==1:
        print(elem,end=' ')
print()

for i in range(0,len(B),2):
    B[i],B[i+1]=B[i+1],B[i]
print(' '.join(map(str,B)))

print(str(C[len(C)-1])+' '+' '.join(map(str,C[0:len(C)-1])))

m=A.count(A[1])
b=A[1]
for elem in A:
    if A.count(elem)>m:
        m=A.count(elem)
        b=elem
print(b)

