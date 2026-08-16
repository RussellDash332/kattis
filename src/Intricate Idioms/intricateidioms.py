D=[];M=[];Z=0
for _ in'.'*(N:=int(input())):
 h,*s=input();p='B';Z+=h>p;b=0
 for i in s:
  if i>'B'==p:p=i
  else:b+=1;p='B'
 D+=[b];M+=[(len(s),s.count('B'))]
print('impossible'if(t:=max(D))>min(M)[0]else sum(t-c for d,(_,c) in zip(D,M))+Z)