inputdata=open('inputdata.txt','r')
B=inputdata.read()
B=B.replace('.',' ').replace(',',' ').replace('!',' ').replace('?',' ')
C=B.split()
for i in range(len(C)):
    C[i]=C[i].lower()
E=dict()
max=None
for elem in C:
    if elem in E:
        E[elem]+=1
    else:
        E[elem]=1
print(E)
for i in range(len(C)):
    if (max==None) or (E[C[i]]>max):
        max=E[C[i]]
        b=C[i]
print('Количество употреблений=',max,'Слово =',b)


