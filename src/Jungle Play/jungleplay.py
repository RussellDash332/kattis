n,k,m=map(int,input().split());s=input();h=[[m]for _ in'.'*n];p=0
for i in range(m-1,-1,-1):h[ord(s[i])-97]+=[i]
for _ in'.'*(k+1):
 for q in h:
  while q[-1]<p:q.pop()
 p=max(q[-1]for q in h)
print([-1,p+1][p<m])