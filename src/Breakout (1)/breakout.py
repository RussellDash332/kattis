b,w,h=map(int,input().split());z=[h]*w
for _ in'.'*b:
 t,p,d=map(int,input().split());u=0;i=t
 while-1<i<w and z[i]:
  for x in range(max(0,i-p),min(w,i+p+1)):
   if z[x]:z[x]-=1
  u+=1;i+=d
 print(u)