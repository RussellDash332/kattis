_,*A=open(0);D=[0]*(p:=2*10**6+67);P=[*D];p-=1
while A:
 s,a,b=map(int,A.pop().split())
 while p>s:p-=1;D[p]=D[p+1];P[p]=P[p+1]+D[p]
 D[s]=max(D[s],D[s+1],1+(P[s+a]-P[s+b+1])/(b-a+1));P[s]=P[s+1]+D[s]
print(D[s])