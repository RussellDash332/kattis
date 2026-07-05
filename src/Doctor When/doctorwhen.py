a,b,c=map(int,input().split());v=1
for h in[*range(1,12),0]:
 for m in range(60):
  for s in range(60):
   i=30*h+(60*m+s)/120;n=6*m+s/10;t=s*6
   for(a,b,c)in((a,b,c),(a,c,b),(b,c,a),(b,a,c),(c,a,b),(c,b,a)):
    if(c-b)%360==(t-n)%360and(b-a)%360==(n-i)%360:print(f'{h or 12:02d}:{m:02d}:{s:02d}');v=0;break
if v:print('Lost!')