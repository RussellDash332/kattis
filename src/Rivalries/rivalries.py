n=int(input());R=range(n);a=[i-1for i in map(int,input().split())];r=[set()for _ in range(n)];m=[-1]*n
for i in R:r[a[i]].add(i)
z=1
while z:
 z=0
 for i in R:
  if not r[i]and i-a[i]and m[a[i]]<0>m[i]:m[a[i]],m[i]=i,a[i];z=1;r[a[a[i]]].discard(a[i])
z=1
while z:
 z=0
 for i in R:
  if i-a[i]and m[a[i]]<0>m[i]:m[a[i]],m[i]=i,a[i];z=1
print(m.count(-1))