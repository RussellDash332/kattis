N=int(input());S,A=input().split();G={}
for _ in'.'*N:s,w,k,*t=input().split();G[s]=(int(w),t)
Q=[(S,0)];T={};V={}
while Q:
 u,b=Q.pop();v=V.get(u,0)
 if b:V[u]=2;T[u]=max(T.get(v,0)for v in G[u][1])+G[u][0]
 elif v%2:print('SAFE')<exit()
 elif v<1:V[u]=1;Q+=[(u,1)]+[(v,0)for v in G[u][1]if v!=A]
print(T[S])