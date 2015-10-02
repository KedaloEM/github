from random import *
output=open('int_data.txt','w')


for i  in range(1000000):
    print(randint(1,100), file=output,end=' ')
output.close()
