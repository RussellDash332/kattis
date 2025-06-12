n,m,k=map(int,input().split());z=set();a=[1]*m
for i in range(n):
 c=[*map(int,input().split())]
 for j in range(m):
  if c[j]==0<a[j]:a[j]=0;z.add(i)
print('yneos'[any(a)or len(z)>k::2])