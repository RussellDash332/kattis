H={}
for s in[*open(0)][1:]:
 n,d,k,*h=s.split()
 for x in h:
  for t in range(*map(int,x.split('-'))):
   v=(d,t)
   if v not in H:H[v]=set()
   H[v].add(n)
V=sorted(H,key=lambda x:(['Su','Mo','Tu','We','Th','Fr','Sa'].index(x[0][:2]),x[1]));_,a,b=max([(H[a]|H[b],a,b)for a in V for b in V if a!=b],key=lambda x:len(x[0]));print(*a);print(*b)