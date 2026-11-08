from heapq import*;I=input;P=[];Q=[];S=0
for _ in'.'*int(I()):t,h=map(int,I().split());P+=(h,-t),
for h,t in sorted(P):
 heappush(Q,t);S-=t
 while Q and S>h:S+=heappop(Q)
print(len(Q))