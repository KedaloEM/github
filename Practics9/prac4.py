Slova=open('en-ru.txt','r')
Words=dict()
Stroka=Slova.readline()
while Stroka!='':
    Stroka=Stroka.rstrip()
    A=Stroka.split('-')
    Stroka=Slova.readline()
    Words[A[0]]=A[1]
Slova.close()
Text=open('input.txt','r')
Perevod=open('output.txt','w')
Stroka=Text.readline()
while Stroka!='':
    Stroka=Stroka.lower()
    for symbol in Words:
        Stroka=Stroka.replace(symbol,Words[symbol])
    print(Stroka,file=Perevod)
    Stroka=Text.readline()
Text.close()
Perevod.close()
