I=lambda:input().split();n,q=map(int,I());C={}
for _ in'.'*q:c,v=I();C[c]=int(v)
m=max(C.values())
if n-m<m:print('Nej');exit()
print('Ja')
B=[[]for _ in'.'*m];p=0
for u,w in sorted(C.items(),key=lambda x:x[1]):
 for _ in'.'*w:B[p:=-~p%m].append(u)
print(' '.join(map(' '.join,B)))