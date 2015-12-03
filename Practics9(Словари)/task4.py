text=open('en-ru.txt','r')
ourWords={}
for line in text:
    line=line.replace(' ','').replace(',',' ').replace('   ','').replace('.','').replace('\t','').replace('\n','').split('-')
    ourWords[line[0]]=line[1]
text.close()

input=open('input.txt','r')
output=open('output.txt','w')
trans=[]
for line in  input.read().split():
     line=line.replace('.','').replace(',',' ')
     line=line.lower()
     if line.lower() in ourWords:
         trans.append(ourWords[line])
     else:
         trans.append(line)

for elem in trans:
    print(elem, end=' ')
    output.write(elem)
    output.write(' ')
output.close()
input.close()
