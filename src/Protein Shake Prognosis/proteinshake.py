from heapq import*;I=lambda:map(int,input().split());N,B,P=I();A=[];Q=[];S=V=P;x=z=0
for _ in'.'*N:b,p=I();A+=(min(p,B-b),b,p),
for d,_,p in sorted(A):d>0!=heappush(Q,p)!=len(Q)>d!=heappop(Q)
Q.sort()
while Q:x+=1;S=max(S,V:=V+Q.pop()-x+1)
for p in sorted(p for _,b,p in A if b+p-B+1<=S):
 if p>S+z:break
 z+=1
print(z)