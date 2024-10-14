m=-1;s=' '.join(open(0).read().split()).split();t=len(s[m]);w=[s.pop()];z=[t]
while s:
 w+=[[]];l=0
 while s and l<=t:s[m]=s[m].replace('.','. ')if w[m]else s[m];l+=bool(w[m])+len(s[m]);w[m]+=[s.pop()]
 w[m]=' '.join(w[m][::m]);z+=[t:=l]
if len(z)>1and z[m]<=z[-2]:w[-2:]=[w[m]+' '*(1+(w[m][m]=='.'))+w[-2]]
print('\n'.join(w[::m]))