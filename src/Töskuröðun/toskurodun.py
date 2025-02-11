n,_,a,b,*c=map(int,open(i:=0).read().split());p=[a,*c,b]
while p:u=p.pop();z=i-i%u;i=n-(z+~(i-z)%[n-z,u][z+u<n])-1
print(i+1)