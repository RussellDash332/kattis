n=int(input());R=range(n*n);M=''.join(input()for _ in'.'*n);Z=0
for i in range(1,1<<2*n+2):
 X={j for j in R if(1<<j//n)&i|(1<<j%n+n)&i}
 for d in range(n):(1<<2*n)&i>0!=X.add(d*-~n);(1<<2*n+1)&i>0!=X.add(-~d*~-n)
 if all(M[j]!='O'for j in X):Z-=(-1)**i.bit_count()*2**sum(M[j]<'O'for j in{*R}-X)
print(Z)