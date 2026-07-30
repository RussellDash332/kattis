def P(a,n,m):return(P(a,n//2,m)*(1+pow(a,n//2,m))+(pow(a,n-1,m)if n%2else 0))%m if n else 0
a,b,x,n,m=map(int,input().split());print((pow(a,n,m)*x+P(a,n,m)*b)%m)