p=input();n=len(s:=input());m=10**9+7;z=0
for w in{s[i:]+s[:i]for i in range(n)}:
 d=[1]+[0]*n
 for i in p:
  for j in range(n)[::-1]:d[j+1]=(d[j+1]+d[j]*(i==w[j]))%m
 z=(z+d[n])%m
print(z)