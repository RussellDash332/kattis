N=int(input());M=10**9+7;a=12;b=0
for _ in'.'*~-N:a,b=6*(a+b)%M,5*a%M
print((a+b)%M if N else 1)