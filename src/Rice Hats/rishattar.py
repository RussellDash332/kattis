from bisect import*;B=[];P=[];z=0
for x,e in sorted([[*map(int,input().split())]for _ in'.'*int(input())],key=lambda x:(x[0],-x[1])):
 if z-x:
  for p,f in P:
   if p<len(B):B[p]=f
   else:B+=[f]
  P=[]
 z=x;P+=[(bisect(B,e-1),e)]
for p,f in P:
 if p<len(B):B[p]=f
 else:B+=[f]
print(len(B))