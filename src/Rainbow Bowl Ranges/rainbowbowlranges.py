n,m,*a=map(int,open(0).read().split());a.sort();p=n-a.pop(0);z=1
for i in a[::-1]:z+=i<n>(p:=p-i-~n)
print(z)