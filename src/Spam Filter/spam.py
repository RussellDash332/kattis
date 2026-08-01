Z=(H:=1,m:=int(input()));p=[k:=0]+[k:=k+i for i in map(int,input())];L=0
for _ in'.'*50:
 S=T=0;M=(H+L)/2
 for i in range(m,len(p)):
  S,T=min((S,T),(p[i-m]-M*(i-m),i-m))
  if p[i]-M*i>S:Z=(T+1,i-T);L=M;break
 else:H=M
print(*Z)