K,N=map(int,input().split());T=[{1}]+[set()for _ in range(N)]
for i in range(1,N+1):
 for j in range(max(i-K+1,0),i):
  for u in T[j]:
   if u:T[i].add((u+i-j+1)%K)
print('yes'if T[-1]=={0}else'no'if 0 not in T[-1] else'maybe')