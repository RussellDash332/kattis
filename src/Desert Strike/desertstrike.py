K,W=map(int,input().split());N=min(W//K,2*W//K//2);z=(K+1)//2*N*(N-1)+K//2*N*N;x,y=K*N,2*N;T=1
while x<=W and y<=2*W//K:u=min((K+T)//2,W-x);z+=y*u;T^=1;y+=1;x+=u
print(((x+y-1)**2-4*z)%(10**9+9))