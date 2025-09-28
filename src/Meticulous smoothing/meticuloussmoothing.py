n,*a=map(int,open(0).read().split());K=sum(a)
for i in range(1,n):a[i]=min(a[i-1]+1,a[i]);a[~i]=min(a[-i]+1,a[~i])
print(K-sum(a))