n=int(input());S=[1]*(L:=int(n**.5)+1);v=n-n%2-1
for p in range(3,L,2):
 if S[p]:
  v=min(v,n-n%p-1)
  for i in range(p,L,p):S[i]=0
print(v)