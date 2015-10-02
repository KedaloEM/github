int1=open('int_data.txt', 'r')
max_freq_i=min_freq_i=0
max_freq=0
min_freq=1000000
koldif=0
A=[]
B=int1.readlines()
for i in range(len(B)):
    A=A+list(map(int, B[i].split()))
for i in range(101):
    print(i,'-',A.count(i),sep=(''))
    if A.count(i)>max_freq:
        max_freq=A.count(i)
        max_freq_i=i
    if (A.count(i)<min_freq)and(A.count(i)!=0):
        min_freq=A.count(i)
        min_freq_i=i
    if A.count(i)!=0:
        koldif+=1
print()
print(max_freq_i,' ',max_freq)
print()
print(min_freq_i,' ',min_freq)
print()
print(koldif)
        
    
    


