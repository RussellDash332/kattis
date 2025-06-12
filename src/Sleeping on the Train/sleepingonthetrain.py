n,t,a,b,*s=map(int,open(0).read().split());s=[a]+s+[b];u=s[0]<=s[1];z=0
for i in range(1,t+1):
 if s[i-1]-s[i]and(s[i-1]<s[i])-u:u^=1;z+=1
print(z+(u!=(s[-2]<s[-1])))