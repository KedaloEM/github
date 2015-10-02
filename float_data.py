from random import *
float1=open('float_data.txt','w')
for i in range(1000000):
    print('%.2f' %(100*random()), file=float1,end=' ')
float1.close()
