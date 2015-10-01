float1=open('float_data.txt','w')
from random import *
for i in range(0,1000000,1):
    float1.write(str(randint(0,9))+str(randint(0,9))+'.'+str(randint(0,9))+str(randint(0,9))+' ')
float1.close()
integer=open('int_data.txt','w')
for i in range(0,1000000,1):
    integer.write(str(randint(0,100))+' ')
integer.close()
