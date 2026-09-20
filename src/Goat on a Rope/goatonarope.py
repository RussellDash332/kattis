from cmath import*;I=lambda:map(float,input().split());L,N=I();N=int(N);P=[complex(*I())for _ in'.'*N];Z=p=0;v=1
while L:u=min(L,abs(q:=P[r:=-~p%N]-P[p]));Z+=phase(q/v)*L;L-=u;p=r;v=q
print(Z)