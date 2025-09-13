n,*v=map(eval,open(0).read().split());z=1;v.sort()
for i in range(n):x=v[~i];v[~i]=z=(v[~i]+z)/2
print(sum(v))