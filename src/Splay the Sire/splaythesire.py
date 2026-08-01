from itertools import*;A,E,D=map(int,input().split())
for i in range(len(C:=[input()for _ in'.'*int(input())])):
 for p in permutations(C,i+1):
  a,e,d=A,E,D;b=f=w=0
  for x in p:
   k=x[0]
   if k<'C':a+=8
   elif k<'E':f-=2
   elif k<'I':e-=10+b;a-=3
   elif k<'M':e-=4+4*b
   elif k<'Q':b+=2
   elif k<'T':b*=2
   elif k<'X':e-=6+b
   elif b>2*a:w=1;break
   a-=max(d+f,0)
   if a<1:w=0;break
   if w or a>0>=e:w=1;break
  if w:print(i+1,*p,sep='\n');exit()
print('Engin vinningsleid!')