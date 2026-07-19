n,x=map(int,input().split());n-=1;x<1<<n!=print('impossible')<exit()
for i in range(n+1):print(*[b:=1<<n-i]*i,x:=x-b*(i>0))