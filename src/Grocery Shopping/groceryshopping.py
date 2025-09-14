C={};P={}
for s in[*open(0)][1:]:c,p=s.split();P[c]=eval(p);C[c]=C.get(c,0)+1
for p,c in sorted((P[x],x)for x in C):print(c,C[c])