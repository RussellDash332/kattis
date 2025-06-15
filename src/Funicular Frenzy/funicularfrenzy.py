n,c,*a=map(int,open(q:=0).read().split());b=(1e9,'impossible')
for i in range(n):
 q+=a[i]
 if q<c*(n-i):b=min(b,(q//c,i))
 q=max(q-c, 0)
print(b[1])