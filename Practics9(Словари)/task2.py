A = set('0123456789')
B = set('02468')
C = set('12345')
D = set('56789')
F= A.difference(B)
G= C.difference(D)
I= F.intersection(G)
J= D.difference(A)
L= B.difference(C)
M= J.intersection(L)
N= I.union(M)
print(N)
