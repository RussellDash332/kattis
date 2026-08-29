G={};I={}
for _ in'.'*int(input()):
 a,c,b=input().split()
 if c<'>':a,b=b,a
 G[b]=G.get(b,[]);G.setdefault(a,[]).append(b);I[a]=I.get(a,0);I[b]=I.get(b,0)+1
Q=[i for i in I if I[i]<1]
for u in Q:
 for v in G[u]:I[v]-=1;I[v]<1!=Q.append(v)
print('im'*(len(Q)<len(G))+'possible')