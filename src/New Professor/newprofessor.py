from bisect import*;Q=sorted(map(int,[*open(Z:=0)][1:]))
while len(Q)>4:[insort(Q,x-1)for x in[Q.pop()for _ in'.'*5]if~-x];Z+=5
print(Z+len(Q))