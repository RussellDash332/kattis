H={}
for s in[*open(0)][1:]:
 n,d,k,*h=s.split()
 for t in map(int,h):
  v=(d,t)
  if v not in H:H[v]=[]
  H[v]+=[n]
d,t=max(H,key=lambda x:len(H[x]));print(f'Your professor should host office hours {d} @ {t:02}:00')