n,m,*v=map(int,open(Z:=0).read().split());a=v[:n];b=v[n:]
for i in'..':
 a,b,n,m=b,a,m,n;k=0
 for x in a:
  while k<m and b[k]<=x:k+=1
  Z+=k<m;k+=1
print(Z)