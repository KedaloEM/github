float1=open('float_data.txt', 'r')
A=[]
summ=0
d=0
B=float1.readlines()   
s=len(B[0].split( ))
for i in range(len(B)):
    A=A+list(map(float, B[i].split( )))  
for i in range(len(A)):
    summ=summ+A[i]
sred=summ/len(A)
for i in range(len(A)):
    d+=(A[i]**2)
sredot=(d/len(A)-sred**2)**0.5
print(sred)
print(sredot)
print(max(A),A.count(max(A)))
print(min(A),A.count(min(A)))
float1.close()    

    
    
