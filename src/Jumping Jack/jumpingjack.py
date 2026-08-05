n,k,*c=map(int,open(0).read().split())
def f(j):
 p=q=r=0
 while 1:
  q+=1
  while q<n and p+j>=c[q]:q+=1
  if q==n:return r+1
  if c[q:=q-1]==p:return 10**9
  p=c[q];r+=1
lo, hi = 1, 10**6+67
while lo < hi:
    if f(mi:=(lo+hi)//2)<k: hi = mi
    else: lo = mi+1
print(lo-1 if f(lo-1)==k else -1)