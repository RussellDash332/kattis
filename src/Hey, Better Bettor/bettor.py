x, p = map(float, input().split())
if p == 0: print(0), exit(0)
q = (100-p)/p; f = (100-x)/100; best = 0; pcw = [1]; pcl = [1]
for _ in range(2500): pcw.append(q*pcw[-1])
for _ in range(21000): pcl.append(pcl[-1]/q)
for w in range(1, 2500):
    old = best
    for l in range(1, 21000): pp = (1-pcl[l])/(pcw[w]-pcl[l]); best = max(best, pp*w-(1-pp)*l*f)
    if old == best: break
print(best)