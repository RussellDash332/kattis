n=int(input());a=b=f=1;M=10**9+7
for i in range(n):a,b,f=b,(a+b)%M,f*-~i%M
print(a*f%M)