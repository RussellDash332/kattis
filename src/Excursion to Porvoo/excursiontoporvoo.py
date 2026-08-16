I=lambda:map(int,input().split())
N,M=I();B=10**18;N-=1;U=[B]*N;R=[];T=B*N
for _ in'.'*M:i,d,c=I();R+=[(c,i:=i-1,d)]
R.sort();Q=[int(input())for _ in'.'*int(input())];Z={}
for x in sorted(Q)[::-1]:
 while R and R[-1][0]>=x:
  _,i,d=R.pop()
  if U[i]>d:T+=d-U[i];U[i]=d
 Z[x]=['impossible',T][T<B]
for x in Q:print(Z[x])