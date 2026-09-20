from bisect import*;N,*a=open(0);L=[];S=[];P=[];N=int(N)
for k in a:l,s=map(int,k.split());P+=[(l,s)];L+=[l];S+=[s]
L.sort();S.sort();Z=0;M=10**9+7;F=[f:=1]+[f:=f*-~i%M for i in range(N)];I=[f:=pow(f,-1,M)]+[f:=f*(N-i)%M for i in range(N)]
for l,s in P:
 for v in(l,s):A=bisect(S,v-1);C=N-bisect(L,v-1)-l//v;Z+=pow(2,A+C,M)*F[B:=~A+N-C]*I[r:=~N+C+v]*I[~B+~r]*(A<v<=N-C)
print(Z%M)