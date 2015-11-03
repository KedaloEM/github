Words = {
            'cat':'кошка',
            'dog':'собака',
            'mouse': 'мышь',
            'house': 'дом',
            'eats': 'ест',
            'in': 'в',
            'too': 'тоже',
            }
input=open('input.txt','r')
output=open('output.txt','w')
B=input.read()
C=B.split()
for i in range(len(C)):
    if C[i] in Words:
        q=Words[C[i]]
        print(q,file=output,end=' ')
    if C[i].lower() in Words:
        if C[i]==C[i].title():
            q=Words[C[i].lower()].title()
            print(q,file=output,end=' ')
    C[i]=C[i][0:(len(C[i])-1):1]
    if C[i] in Words:
        q=Words[C[i]]+'.'
        print(q,file=output,end=' ') 
        print('',file=output)
    if C[i].lower() in Words:
        if C[i]==C[i].title():
            q=Words[C[i].lower()].title()+'.'
            print(q,file=output,end=' ') 
            print('',file=output)
input.close()
output.close()

