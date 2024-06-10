n=int(input());M=10**9+7;f=125000001
for i in range(20):f*=n-i;f%=M
print(f)