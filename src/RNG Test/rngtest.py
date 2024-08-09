def ps(a,n,m):return(ps(a,n//2,m)*(1+pow(a,n//2,m))+(pow(a,n-1,m)if n%2else 0))%m if n else 0
a,b,x,n,m=map(int,input().split());print((pow(a,n,m)*x+ps(a,n,m)*b)%m)