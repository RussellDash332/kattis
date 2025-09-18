n,m=map(int,input().split());d=[0]+[1e18]*n
for i in range(n):
 s,*v=map(int,input().split())
 for j,p in enumerate(v):d[i+j+1]=min(d[i+j+1],d[i]-p+s)
print(d[n])