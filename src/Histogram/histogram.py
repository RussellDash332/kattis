n,s,k,*a=map(int,open(0).read().split());f=[0]*n
for i in a:f[~-i//s]+=1
F=max(f)
for i in range(F):print(''.join('#.'[i+j<F]for j in f))
print('-'*n)