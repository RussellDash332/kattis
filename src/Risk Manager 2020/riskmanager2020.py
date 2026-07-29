n,k=map(int,input().split());i=0
for _ in'.'*n:
 _,*s=input().split()
 if len({v.split('_')[0]for v in s})==k:print(i:=i+1,*s)