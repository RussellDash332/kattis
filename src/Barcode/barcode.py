R=range(3,x:=10**6,2);f=lambda n:n>=p and n//p+f(n//p);P={2,*R}
for n in R[:500]:P-={*range(n*n,x,2*n)}
for i in[*open(0)][1:]:
 n,m=map(int,i.split());a=b=1
 for z in[1]*n:a,b=b,(a+b)%m
 for p in P:z=z*pow(p,f(n)-2*f(n>>1),m)%m
 print((~n//2+b+z,b)[n&1]%m)