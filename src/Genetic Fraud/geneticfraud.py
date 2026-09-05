for _ in'.'*int(input()):
 n=int(input());s=input().encode();d=[z:=0]*-~n;l=-~n//2
 for u in input().encode():
  e=[0]*-~n
  for i,v in enumerate(s):
   if abs(u-v)<2:
    e[i+1]=d[i]+1
    if e[i+1]>=l:z=1;break
  if z:break
  d=e
 print('NPEOGSAITTIIVVEE'[z::2])