from itertools import*;C=complex;n,x,y,*A=map(int,open(0).read().split());F=lambda u,v,w:((v-u).conjugate()*(w-u)).imag;Z=[0]*n
for i,j,k in combinations(range(n),3):
 t=F(r:=C(*A[2*k:][:2]),p:=C(*A[2*i:][:2]),q:=C(*A[2*j:][:2]));u=F(r,c:=x+y*1j,q)/t;v=F(r,p,c)/t
 if v>0<u:Z[i]=u;Z[j]=v;Z[k]=1-u-v;print(*Z);break