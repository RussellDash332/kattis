N,K=map(int,input().split());X=[*map(int,input().split())];W=[*map(int,input().split())]
def f(b):
 if b<1:return N
 z=9e9
 for i in range(N):
  if b&(1<<i):z=min(z,f(b^(1<<i))+X[i])
  for j in range(i):
   if b&(u:=2**i+2**j)==u and W[i]+W[j]<=K:z=min(z,f(b^u)+max(X[i],X[j]))
 return z
print(2*f(2**N-1))