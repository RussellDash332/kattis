M=10**9+7;a=k=r=0;t='1'
for i in input():s=i>t;k+=i==t;a+=a*s+(i!=t)*(r+2*k)*pow(2,r-1,M);a%=M;r+=s
print(a)