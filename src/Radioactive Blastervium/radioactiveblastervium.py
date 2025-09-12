n,t,*p=map(int,open(z:=0).read().split())
for i in range(1,1<<n):
 u=b=1
 for j in range(n):
  if i&(1<<j):u*=p[j];b+=1
 z+=t//u*(-1)**b
print(z)