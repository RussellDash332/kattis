A=map(int,open(0).read().split());I=A.__next__
for n in A:
 m=I();G=[set()for _ in' '*-~n];V=set()
 for _ in' '*m:G[a:=I()]|={b:=I()};G[b]|={a}
 Z=max(map(len,G))<4
 for i in range(-~n):
  if{i}-V:
   q=[i]
   for u in q:
    if{u}-V:V|={u};q+=G[u]
   c=[u for u in q if 2<len(G[u])];Z*=all(len(G[i]&{*G[j],j})>1for i in c for j in c)
 print('YNEOS'[Z::2])