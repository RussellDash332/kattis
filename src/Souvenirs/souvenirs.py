G,c,n=map(int,input().split());T=[];N=n+1;K=999;D=[0]*N*K*-~c
for _ in'.'*n:m,p,s=input().split();T+=[(t:='yts'.index(m[-1]),p:=int(p),v:=int(s),(G-v+(0,p//2,p-1)[t])//p*p*N-N*K)]
for m in range(n)[::-1]:
 t,p,v,q=T[m]
 for g in range(c+1):
  for s in range(K):
   b=D[u:=g*N*K+s*N+m+1]
   if(s>=v)*(b<1+D[u-v*N]):b=1+D[u-v*N]
   if(t!=2 or s<v)*(b<1+D[u+q])*g:b=1+D[u+q]
   D[u-1]=b
print(D[c*N*K])