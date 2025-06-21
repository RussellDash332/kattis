n=int(input());p=[1]*n;D=[];R=[]
for i in range(n):
 d,r=map(int,input().split());D.append(d);R.append(r)
 for j in range(i):
  if D[i]-D[j]>max(R[i],R[j]):p[i]=max(p[i],p[j]+1)
print(n-max(p))