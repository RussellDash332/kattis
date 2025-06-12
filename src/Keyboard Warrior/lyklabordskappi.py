n,l,t=map(int,input().split());v=[];s=0;o=[]
for i in input().split():
 u=len(i)+1
 if s+u<=l*t:v.append(i);s+=u
 elif u<=l*t:o.append([*v]);v=[i];s=u
 else:print('/ff');exit()
o.append(v)
for i in o:print(*i)