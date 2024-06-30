n,*a=map(int,open(0).read().split());r={e:i+1for i,e in enumerate(sorted(a))};d=[0]*2*n
for i in a:d[r[i]]=d[r[i]-1]+1
print(n-max(d))