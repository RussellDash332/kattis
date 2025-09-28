V=set();I=input
for _ in'.'*int(I()):(x,y),*P=sorted([*map(int,I().split())]for _ in'.'*int(I()));V.add(tuple((a-x,b-y)for a,b in P))
print(len(V))