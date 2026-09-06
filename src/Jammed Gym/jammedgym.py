from cmath import*;from heapq import*;n=int(input());t=[*map(int,input().split())];m=int(input());q=[*map(int,input().split())];h=[[]for _ in range(101)];D=[1e9]*-~n*-~m;p=[(0,m)];D[m]=0
for i in range(m):h[q[i]]+=[i]
P=[exp(2j/m*pi*i)for i in range(m)]+[0];m+=1
while p:
 d,v=heappop(p);c=v//m;i=v%m
 if(c<n)*(d==D[v]):
  for k in h[t[c]]:
   if D[u:=c*m+m+k]>(x:=d+abs(P[i]-P[k])):D[u]=x;heappush(p,(x,u))
print(min(D[-m:]))