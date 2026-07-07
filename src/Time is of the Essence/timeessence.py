from math import*;v=input().split();k=[*map(int,v[2::2])];u=v[1::2];t=int(input())
while len(u)>2:t/=k.pop();u.pop()
b=-~int(2*t)//2;x,y=divmod(b,k[0]);u,v=u;print(-~int(2*t/k[0])//2,u,x,u,y,v)