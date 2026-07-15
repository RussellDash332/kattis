k,n=map(int,input().split());m=int(n**(1/k));t=m**k;p=m*k
while t<n:p+=1;t=t*-~m//m
print(p)