I=lambda:map(int,input().split())
for _ in'.'*int(input()):
 n,m=I();g=[[]for _ in'.'*n];d=[0]*n
 for _ in'.'*m:a,b=I();g[a-1]+=[b-1];d[b-1]+=1
 q=[i for i in range(n)if d[i]<1];z=[*q];t=len(q)>1
 while q:
  r=[]
  for u in q:
   for v in g[u]:d[v]-=1;d[v]<1!=r.append(v)
  t|=len(r)>1;q=r;z+=r
 if len(z)<n:print('recheck hints')
 elif t:print('missing hints')
 else:print(*(i+1for i in z))