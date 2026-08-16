n,*t=map(int,open(0).read().split());s=sorted(t)
if s==t:print(0);exit()
g=[[]for _ in'.'*n]
for i in range(n):
 if s[i]-t[i]:g[s[i]-1]+=[(t[i]-1,i)]

# hierholzer
vis = [0]*n; p = []; r = []; idx = [0]*n
for s in range(n):
    if g[s] and vis[s]<1:
        ans, stk, es = [], [s], []
        while stk:
            u = stk[-1]; vis[u] = 1
            if idx[u] < len(g[u]):  v, e = g[u][idx[u]]; stk.append(v); es.append(e); idx[u] += 1
            else:                   stk.pop(); es and ans.append(es.pop())
        p += ans; r += [ans[-1]]

print(1+(u:=len(r)>1),len(p),*(i+1for i in p),*[len(r),*(i+1for i in[r[0]]+r[1:][::-1])]*u)