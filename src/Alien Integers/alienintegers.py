from bisect import*;s=[*map(int,input())];n=len(s);d=sorted({*range(10)}-{*s})
if not d:print('Impossible'),exit()
if d==[0]:print(0);exit()
b=bisect(d,s[0])
if b==len(d):u=[d[0]or d[1]]+[d[0]]*n
else:u=[d[b]]+[d[0]]*(n-1)
b=bisect_left(d,s[0])-1
if b<0 or s[0]<2:l=[d[-1]]*(n-1)
else:l=[d[b]]+[d[-1]]*(n-1)
s=int(''.join(map(str,s)));u=int(''.join(map(str,u)));l=int(''.join(map(str,l or[0])))
if u-s==s-l:print(l,u)
elif u-s>s-l:print(l)
else:print(u)