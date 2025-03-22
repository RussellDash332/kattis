n,t,*a=map(int,open(0).read().split());m=998244353;z=t-sum(a)+1;u=z+n
for i in a[:-1]:u+=i-1;z=z*u%m
print(z)