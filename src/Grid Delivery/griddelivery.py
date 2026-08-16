from bisect import*;R,C=map(int,input().split());B=[]
for r in range(R):
 s=input()
 for c in range(C):
  if s[c]<'_':
   if(p:=bisect(B,~c))<len(B):B[p]=-c
   else:B+=[-c]
print(len(B))