for _ in range(int(input())):
 m=s=n=t=z=0
 for i in map(int,input().split()[1:]):m=max(m,s:=max(0,s+i));n=min(n,t:=min(0,t)+i);z+=i
 print(max(m,z-n))