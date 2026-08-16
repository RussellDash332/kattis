n,*p=map(eval,open(0));p={1<<i:p[i]for i in range(n)};D=[0]*2**n
for b in range(1<<n):
 if b.bit_count()>2:
  r=x=b;w=k=z=1;s=0
  while r:w*=p[u:=r&-r];k*=1-p[u];r^=u
  while x:q=p[u:=x&-x]/(1-p[u]);t=w/q+k*q;z+=t*D[b^u];x^=u;s+=t
  D[b]=z/s
print(D[-1])