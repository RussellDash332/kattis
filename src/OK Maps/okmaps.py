N,M=map(int,input().split());A=[[0]*N for _ in'.'*N];x=y=q=0;p=1;A[0][0]=1
for _ in'.'*(M+2):x+=p;y+=q;A[x][y]=1;p,q=q,p
for r in A:print(*r,sep='')