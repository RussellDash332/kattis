def M(I): h=lambda a,b:0 if a[1]<b[0]or b[1]<a[0]else[min(a[0],b[0]),max(a[1],b[1])]; return [r:=[],[[r.pop(),r.append(k)]if r and(k:=h(r[-1],j))else r.append(j)for j in sorted(I)]][0]
m=[[*map(int,input().split())]for _ in'.'*int(input())]
t=set()
for a,b in m:t.add(a),t.add(b)
k=M(m)[::-1]
for a,b in zip(t:=sorted(t),t[1:]):
 while k and k[-1][1]<b:k.pop()
 if k and k[-1][0]<=a:print(a,b)