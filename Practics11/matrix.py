__author__ = 'student'
class Matrix:
    def __init__(self, m, n=None):
       if type(m)!=list:
            if type(m)!=int:
                raise ValueError()
        if type(n)!=int:
            if n!=None:
                raise ValueError()
        if type(n)==int and n<1:
            raise ValueError()
        if type(n)==int and len(n)<1:
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
        if self.m==other.m and (self.n==other.n):
            for i in range(self.m):
                for i in range(self.n):
                    if self[i][j]!=other[i][j]:
                        ravn=0
                        break
        else:
            raise Exception()
        return(ravn)

    def __set__(self, i,j, value):
        if (i>self.m or j>self.n) or (i<1 or j<1) or (not isinstance(n,int) or not isinstance(m,int)):
            raise Exception()
        else:
            self.matr[i-1][j-1]=value

    def get_m(self):
        return(self.m)
    def get_n(self):
        return(self.n)
    def get_size(self):
        razmer=[self.m,self.n]
        return(razmer)

    def __mul__(self, other):
        if self.n!=other.m:
            raise Exception
        else:
            for i in range(self.m):
                k=0
                for j in range(self.n):
                    umnozh[i][k]+=self.matr[i][j]*other.matr[j][k]

                    k+=1



