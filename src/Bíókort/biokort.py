n,m,k=map(int,input().split());p=[0]*(10**7+1);s=n;t=0;z=(1e18,0)
for _ in'.'*n:p[u:=int(input().split()[1])]+=1;t+=u
for i in range(10**6+1):t-=i*p[i];s-=p[i];z=min(z,(i*k+(t-s*i)*m,i))
print(z[1],z[0])