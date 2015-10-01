float1=open('float_data.txt','r')
output=open('output.txt','w')
c=(float1.read(6))
s=0
d=0
i=0
m=float(c)
mal=float(c)
while len(c)>0:
    if float(c)>m:
        m=float(c)
        r=i
    if float(c)<mal:
        mal=float(c)
        w=i
    s+=float(c)
    i+=1
    d+=(float(c))**2
    c=(float1.read(6))
c=float1.read(6)
q=s/1000000
print(q)
print(((d/1000000)-(q)**2)**0.5)
float1.close()
print(m,r)
print(mal,w)


