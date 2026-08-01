P=[3**i for i in range(101)];S=20001
N,*V=map(int,open(0).read().split())
A=V[:N];B=[-i for i in V[N:]]
M=min(A+B);D=[3**N]*S;F=[0]*S;D[0]-=1;F[0]=1
C=lambda x,i:x-x%P[-~i]+x%P[i]
for i in range(N):
 E=[3**N]*S;a=A[i]-M;b=B[i]-M;u=N-1-i;G=[0]*S
 for j in range(S-a):
  if F[j]:E[j+a]=min(E[j+a],C(D[j],u));G[j+a]=1
 for j in range(S-b):
  if F[j]:E[j+b]=min(E[j+b],C(D[j],u)+3**u);G[j+b]=1
 D=E;F=G
s=''
for i in range(S):
 Z=min([D[-M*N+x]for x in(-i,i)if-S<=-M*N+x<S and F[-M*N+x]]or[''])
 if Z!='':
  for _ in'.'*N:s+='AB'[Z%3];Z//=3
  print(s[::-1]);break