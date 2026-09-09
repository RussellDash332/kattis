W={};N=int(input());Z=0
for _ in'.'*N:a,b,c=input();W.setdefault(a+b,set()).add(c)
for a,b in W:
 for c,d in W:
  if(len({a,b,c,d})==4)*(a+c in W)*(a+d in W)*(b+d in W):
   for x in W[a+b]:
    if x+d in W:
     for y in W[c+d]:
      if x+y in W:
       for p in W[a+c]&W[x+d]:
        for q in W[b+d]:
         if p+q in W and len(u:={a,b,c,d,p,q,x,y})>7:Z+=len((W[x+y]&W[a+d]&W[p+q])-u)
print(Z)