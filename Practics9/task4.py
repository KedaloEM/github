Words={}
enru=open('en-ru.txt','r')
input=open('input.txt','r')
output=open('output.txt','w')
S=enru.readlines()
P=()
for elem in S:
    P=elem.split('-')
    Words[P[0]]=P[1]
B=input.read()
C=B.split()
print(C)
for i in range(len(C)):
    if C[i] in Words:
        q=Words[C[i]]
        print(C[i],q)
        print(q,file=output,end=' ')
    elif C[i].lower() in Words:
        if C[i]==C[i].title():
            q=Words[C[i].lower()].title()
            print(q,file=output,end=' ')
    elif C[i][0:(len(C[i])-1):1] in Words:
        q=Words[C[i][0:(len(C[i])-1):1]]+'.'
        print(q,file=output,end=' ') 
        print('',file=output)
    elif C[i][0:(len(C[i])-1):1].lower() in Words:
        if C[i][0:(len(C[i])-1):1]==C[i][0:(len(C[i])-1):1].title():
            q=Words[C[i][0:(len(C[i])-1):1].lower()].title()+'.'
            print(q,file=output,end=' ') 
            print('',file=output)
    else:
        print(C[i],file=output)
input.close()
output.close()

