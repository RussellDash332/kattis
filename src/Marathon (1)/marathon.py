m=5e6;n,*s=map(int,open(0).read().split());d=max(*((b-a)/2for a,b in zip(s,s[1:])),s[0],m-s[-1]);s+=[9e9];z=p=q=r=0
while-r>~n:
 x=s[r]
 if x-d<=p:q=max(q,x+d);r+=1
 else:
  p=q;z+=1
  if~-(x-d<=q<m):break
print(f'%.1f'%d,n-z)