w=[s.strip()for s in open(0)][1:];m=[[]for _ in'.'*26];d=[0]*26;t='';I='impossible'
for a,b in zip(w,w[1:]):
 r=1
 for p,q in zip(a,b):
  if p!=q:m[ord(p)-97].append(v:=ord(q)-97);d[v]+=1;r=0;break
 if r and len(a)>len(b):print(I);exit()
q=[i for i in range(26)if d[i]<1]
for i in q:
 t+=chr(i+97)
 for j in m[i]:d[j]-=1;d[j]<1!=q.append(j)
print([I,t][len(t)>25])