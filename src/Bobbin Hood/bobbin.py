from bisect import*;P,N,*A=map(int,open(0));S=[p:=0]+[p:=p+i for i in sorted(A)];Z=(P,1)
for i in range(N):
 if(b:=bisect(S,~-P+S[i]))<=N:X,Y=S[i+1]-S[i],S[b]-S[b-1];Z=min(Z,(Y-X,-X))
x,y=Z;print(-y,x-y)