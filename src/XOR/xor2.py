for s in[*open(0)][1:]:
 a,n=map(int,s.split());b=0
 for i in range(64,-1,-1):
  p=((a^b)|(2**i-1))-(2**i-1);z=0
  if 2**i>=n:z=1
  elif p%n<1or p%n>(p+2**i-1)%n:z=1
  if 1-z:b+=1<<i
 print(min(a,a^n,[b,a][a<n]))