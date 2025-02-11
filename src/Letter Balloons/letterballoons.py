k,u=map(int,input().split());s=[]
for _ in range(u):
 a=input()
 if len(a)==len({*a})and max(a)<chr(65+k):s.append(a)
v=len(s);g=[set()for _ in'.'*v]
for i in range(v):
 for j in range(i):
  if not {*s[i]}&{*s[j]}:g[i].add(j),g[j].add(i)
def bk(r,p,x):
 if not p and not x: return len(r)
 a=0
 for i in p:u=i;break
 for i in x:u=i;break
 for w in[*p]:
  if w in g[u]: continue
  r.add(w);a=max(a,bk(r,p&g[w],x&g[w]));r.discard(w),p.discard(w),x.add(w)
 return a
print(bk(set(),{*range(v)},set()))