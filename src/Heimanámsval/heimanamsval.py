n,k,*a=map(int,open(0).read().split());M=10**9+7;F=1;A={*a};Z=(pow(2,n,M)-(0in A))%M
for i in range(10**5):
 F=F*(n-i)*pow(i+1,-1,M)%M
 if i+1in A:Z=(Z-F)%M
print(Z)