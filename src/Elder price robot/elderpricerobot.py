n,*a=map(int,open(0).read().split());z=['infinity']*n;s=[]
for i in range(n):
 while s and s[-1][1]>=a[i]:x=s.pop()[0];z[x]=i-x
 s+=[(i,a[i])]
print(*z)