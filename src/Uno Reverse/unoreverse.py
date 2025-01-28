K,N=map(int,input().split());T=[{(1,1)}]+[set()for _ in range(N)]
for i in range(1,N+1):
 for j in range(i):
  for u,p in T[j]:
   if u:q=p*(1-(i-j)%2*2);T[i].add(((u+q)%K,q))
U={x[0]for x in T[-1]};print('YES'if U=={0}else'NO'if 0 not in U else'MAYBE')