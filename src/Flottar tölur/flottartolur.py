K,x=map(int,input().split());M=10**9+7;R=range
if x<1:print((9*pow(10,K-1,M)-pow(9,K,M))%M);exit()
A=B=C=D=0
while x%2<1:A+=1;x//=2
while x%3<1:B+=1;x//=3
while x%5<1:C+=1;x//=5
while x%7<1:D+=1;x//=7
if x>1 or C+D>K:print(0);exit()
N=10**6;F=[f:=1]+[f:=f*-~i%M for i in range(N)];I=([f:=pow(f,-1,M)]+[f:=f*(N-i)%M for i in range(N)])[::-1];T=F[K]*I[C]*I[D]*I[K:=K-C-D]%M;A+=1;B+=1;L=A*B;P=[0]*L;Q=[1]+[0]*~-L
for a,b in((0,0),(1,0),(0,1),(2,0),(1,1),(3,0),(0,2)):
 if a<A and b<B:P[a*B+b]=1
def m(a,b):
 c=[0]*L
 for i in R(L):
  for j in R(L):
   if i//B+j//B<A and i%B+j%B<B:c[i+j]=(a[i]*b[j]+c[i+j])%M
 return c
while K:
 if K%2:Q=m(Q,P)
 P=m(P,P);K>>=1
print(Q[-1]*T%M)