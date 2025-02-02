n,k=map(int,input().split());z=0
while n>k:
 a=e=0;c=1
 while c*k+1<=n:
  a=a*k+1;c=c*k+1;e+=1
  if e==k:print(a+n-c),exit()
 z+=a;n-=c
print(z)