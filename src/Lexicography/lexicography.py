fact = [1]
for _ in range(16): fact.append(fact[-1]*len(fact))
import sys
for l in sys.stdin:
    s, k = l.split()
    if s == '#': break
    ctr = [0]*26; k = int(k)
    for i in s: ctr[ord(i)-65] += 1
    s = len(s); res = []
    while s:
        cnt = fact[s]
        for i in ctr: cnt //= fact[i]
        cur = 0
        for i in range(26):
            if not ctr[i]: continue
            if (new:=cur+cnt*ctr[i]//s) >= k: break
            cur = new
        k -= cur; res.append(chr(i+65)); ctr[i] -= 1; s -= 1
    print(''.join(res))