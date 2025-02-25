t,c,o,d,i=map(int,input().split());x=20*i+12*d+8*o+6*c+4*t;D=[1]+[0]*600
for a,b in zip((t,c,o,d,i),(4,6,8,12,20)):
 for _ in range(a):
  E=[0]*600
  for v in range(x+1):
   for k in range(1,b+1):E[v+k]+=D[v]
  D=E
print(*sorted(range(t+c+o+d+i,x+1),key=lambda x:-D[x]))