G={};N=int(input());S=input();Q=[(S,0)];V={0}
for _ in'.'*N:a,b=input().split();G[a]=G.get(a,[]);G[a]+=[b]
for v,d in Q:
 if d and v==S:print(d);exit()
 if v in V:continue
 V.add(v);v in G and Q.extend((x,d+1)for x in G[v])
print('NO BLACK HOLE')