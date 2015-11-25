__author__ = 'student'
class Matrix:
    def __init__(self, m, n=None):
        if (type(m)!=list) and (type(m)!=int):
            raise ValueError()
        if (type(n)!=int) or (n!=None):
            raise ValueError()
        if (type(n)==int and n<1) or  (type(m)==int and m<1):
            raise ValueError()
        if (type(n)==int and len(n)<1) or (type(m)==int and len(m)<1):
            raise ValueError()
        if n==None:
            matr=m
            self.matr=m
            self.stroki=len(matr)
            self.stolbcy=len(matr[0])
        else:
            self.stroki=m
            self.stolbcy=n
            self.matr=[[0]*n for i in range(m)]


    def get(self, i,j):
        if (i>self.stroki or j> self.stolbcy) or (i<1 or j<1):
            raise Exception()
        else:
            return(self.matr[i-1][j-1])

    def __add__(self, other):
        if (self.stroki!=other.stroki) or (self.stolbcy!=other.stolbcy):
            raise ValueError()
        else:
            Summ=[[0]*(int(self.stroki)) for i in range(int(self.stroki))]
            for i in range(int(self.stroki)):
                for j in range(int(self.stolbcy)):
                    Summ[i][j]=self.matr[i][j]+other.matr[i][j]
        return(Matrix(Summ))
    def __eq__(self, other):
        ravn=1
        if self.stroki==other.stroki and (self.stolbcy==other.stolbcy):
            for i in range(self.stroki):
                for j in range(self.stolbcy):
                    if self.matr[i][j]!=other[i][j]:
                        ravn=0
                        break
        else:
            raise Exception()
        return(ravn)

    def __set__(self, i,j, value):
        if (i>self.stroki or j>self.stolbcy) or (i<1 or j<1) or (not isinstance(i,int) or not isinstance(j,int)):
            raise Exception()
        else:
            self.matr[i-1][j-1]=value

    def get_m(self):
        return(self.stroki)
    def get_n(self):
        return(self.stolbcy)
    def get_size(self):
        razmer=[self.stroki,self.stolbcy]
        return(razmer)

    def __mul__(self, other):
        if self.stolbcy!=other.m:
            raise Exception
        else:
            umnozh=[[0]*int(other.stolbcy) for i in range(self.stroki)]
            for i in range(self.stroki):
                k=0
                for j in range(self.stolbcy):
                    umnozh[i][k]+=self.matr[i][j]*other.matr[j][k]

                    k+=1



