n,m=map(int,input().split());D=[0]*2**n;D[-1]=1
for _ in'.'*m:
 i,j,p=map(eval,input().split());i-=1;j-=1
 for b in range(1<<n):
  if b&(1<<i)and b&(1<<j):D[b^(1<<j)]+=D[b]*p;D[b]*=1-p
for i in range(n):print(sum(D[j]for j in range(1<<n)if j&(1<<i)))