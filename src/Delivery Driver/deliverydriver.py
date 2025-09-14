a,b,c,n,*m=map(int,open(0).read().split());v=[0,a,b,a,0,c,b,c,0];d=[0]*3*n;d[::n]=m[::n]
for i in range(1,n):
 for j in range(3):d[u]=m[u:=n*j+i]+max(d[n*k+i-1]-v[3*k+j]for k in range(3))
print(max(d))