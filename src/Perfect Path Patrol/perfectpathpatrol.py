n=int(input());p=[[]for _ in'.'*n]
for _ in'.'*(n-1):a,b,w=map(int,input().split());p[a-1]+=[w];p[b-1]+=[w]
print(sum(max((s:=sum(q))%2,2*max(q)-s)for q in p)//2)