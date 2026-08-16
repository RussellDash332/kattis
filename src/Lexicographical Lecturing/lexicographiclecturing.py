n,l=map(int,input().split());M=[input()for _ in'.'*n];Z=[*range(l)]
for i in range(n-1):
 s=M[i];t=M[i+1];p=0
 for j in range(l):
  while p<j:p+=1
  if p<l and s[p]>t[p]:Z[j]=l;continue
  while p<l and s[p]==t[p]:p+=1
  Z[j]=max(Z[j],p)
print(*min([(i+1,Z[i]+1)for i in range(l)if Z[i]<l],key=lambda x:x[1]-x[0]))