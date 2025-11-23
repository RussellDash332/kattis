n,p=map(int,input().split());z=1;m=n
while n:z*=n%p+1;n//=p
print(m+1-z)