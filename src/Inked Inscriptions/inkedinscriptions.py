N,*A=map(int,open(0).read().split());x=y=1;A=[*enumerate(A,1)]
for _ in'.'*N:A.remove(k:=min(A,key=lambda t:abs(t[0]-x)+abs(t[1]-y)));print(*k);x,y=k