n=int(input());s=0;t=9
while n:k=(10**t-1)//9;s+=n//k;n%=k;t-=1
print(s)