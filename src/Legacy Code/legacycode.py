P=[];G={}
for _ in'.'*(N:=int(input())):
 p,k=input().split();P+=[p]*('PROGRAM'==p.split(':')[2])
 for q in input().split():G.setdefault(q,[]).append(p)
V={*P};[v in V or V.add(v)!=P.append(v)for u in P for v in G.get(u,[])];print(N-len(P))