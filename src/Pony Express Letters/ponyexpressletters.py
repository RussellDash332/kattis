s=''.join(open(0).read().split()[1:])
for w in['attack','die','fever','hunger','happy','antidisestablishmentarianism']:
 u=['']*(l:=min(n:=len(s)//2,m:=len(w)))
 for j in range(m):u[j%n]+=w[j]
 print('NY'[any(all(a in b*2for a,b in zip(u,(s[(2*i+2*j)%(2*n):][:2]for j in range(l))))for i in range(n))])