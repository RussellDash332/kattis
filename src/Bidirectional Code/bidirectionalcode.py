s=int(input());p=[]
while s:
 u=s
 while 1:
  v='';n=len(t:=str(u))
  for i in range(n//2):v+=min(t[i],t[~i])
  w=int(v+n%2*t[n//2]+v[::-1]);u-=1
  if w and(not v or int(v[0])):p.append(w);s-=p[-1];break
print(len(p),*p)