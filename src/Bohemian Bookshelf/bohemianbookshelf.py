I=input;N,H,W=map(int,I().split());E=[]
for i in range(N):h,t=map(int,input().split());E+=[(h,t,i+1)]
for i in range(N):
 P=[E[j]for j in range(N)if j-i];X=E[i][0];Y=E[i][1];U=[];S=[E[i][2]];V=set();A=W-X;B=H-Y;z=0
 for j in range(N-1):
  if P[j][0]>max(H,X):z=1
  if X>=P[j][0]>H:S+=[P[j][2]];V.add(j);B-=P[j][1]
  if H>=P[j][0]>X:U+=[P[j][2]];V.add(j);A-=P[j][1]
 if W-X<1or H<Y or z or sum(p[1]for p in P)>W+H-X-Y:continue
 P=[P[j]for j in range(N-1)if j not in V];F=sum(p[1]for p in P);D=[1]+[0]*min(B,F-1+bool(U));V=set()
 for j in range(len(P)):
  for k in range(len(D)-P[j][1]-1,-1,-1):
   if D[k] and not D[k+P[j][1]]:D[k+P[j][1]]=j+1
 for k in range(len(D)):
  if D[k]:s=k
 while s:k=D[s]-1;S+=[P[k][2]];s-=P[k][1];V.add(k)
 for j in range(len(P)):
  if j not in V:U+=[P[j][2]]
 if W-X>=sum(E[u-1][1]for u in U)and max(max(E[u-1][0]for u in U),sum(E[s-1][1]for s in S))<=H:print('upright',*U);print('stacked',*sorted(S,key=lambda k:-E[k-1][0]));exit()
print('impossible')