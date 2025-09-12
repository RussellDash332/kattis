R,S,N,*a=map(int,open(0).read().split());Z=T=0
while Z%S-R and T<N:Z+=a[T];T+=1
print([-1,T][Z%S==R])