from math import*;n,*a=map(float,open(0).read().split());a.sort();a=sorted([sum(a)/n,a[int(n)//2],exp(sum(map(log,a))/n)])
while abs(a[0]-a[2])>1e-6:a=sorted([sum(a)/3,a[1],(a[0]*a[1]*a[2])**(1/3)])
print(a[0])