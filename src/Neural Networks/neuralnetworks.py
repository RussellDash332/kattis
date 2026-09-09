M=998244353;N,*A=map(int,open(0).read().split());Z=1;P=[1]
for _ in range(max(A)):P+=[P[-1]*2%M]
for x,y in zip(A,A[1:]):
 F=[f:=1]+[f:=f*-~i%M for i in range(x)];I=([f:=pow(f,-1,M)]+[f:=f*(x-i)%M for i in range(x)])[::-1];z=0
 for i in range(x+1):z+=(1-i%2*2)*F[x]*I[i]*I[x-i]*pow(P[x-i]-1,y,M)%M
 Z=Z*z%M
print(Z)