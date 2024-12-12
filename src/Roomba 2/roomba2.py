r,d=map(int,input().split())
if r==1:
 for c in range(d):print(0,c)
 for c in range(d-2,-1,-1):print(0,c)
elif d==1:
 for c in range(r):print(c,0)
 for c in range(r-2,-1,-1):print(c,0)
elif r%2==0:
 k=1;i=0;j=d
 for c in range(d):print(0,c)
 for _ in range(r-1):
  j-=k;k=-k;i+=1
  for _ in range(d-1):print(i,j);j+=k
 for c in range(r-1,-1,-1):print(c,0)
elif d%2==0:
 k=1;i=0;j=r
 for c in range(r):print(c,0)
 for _ in range(d-1):
  j-=k;k=-k;i+=1
  for _ in range(r-1):print(j,i);j+=k
 for c in range(d-1,-1,-1):print(0,c)
else:
 for c in range(r):print(c,0)
 for c in range(1,d):print(r-1,c)
 i=r-2;j=d;k=1
 for _ in range(d-3):
  k=-k;j-=1;print(i,j)
  for _ in range(r-2):i+=k;print(i,j)
 k=1
 for _ in range(r-1):
  print(i,3-k);print(i,k);i-=1;k=3-k
 print(0,1);print(0,0)