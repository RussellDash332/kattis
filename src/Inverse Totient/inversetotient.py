from random import randint
def miller_rabin(p):
    if p == 2: return 1
    if p % 2 == 0: return 0
    if p == 3: return 1
    d, s = p-1, 0
    while d % 2 == 0: d //= 2; s += 1
    for _ in range(3):
        x = pow(randint(2, p-2), d, p)
        if x == 1 or x == p-1: continue
        ok = 0
        for _ in range(s):
            x = x*x%p
            if x == 1: return 0
            if x == p-1: ok = 1; break
        if not ok: return 0
    return 1

T = int(input())
if T == 1: print(1), exit(0)
if T%2: print(-1), exit(0)

# idea: if p divides N, then p-1 divides T where p is prime
P = []
for i in range(1, 10**7):
    if T%i==0:
        if miller_rabin(i+1): P.append(i+1)
        if miller_rabin(T//i+1): P.append(T//i+1)
P = sorted(set(P), reverse=True)

# now we simply backtrack all the primes
# if N = p1^k1 p2^k2 ... pm^km then T = p1^(k1-1) p2^(k2-1) ... pm^(km-1) * (p1-1)(p2-1)...(pm-1)
INF = 10**18
def bt(idx, curr_t, curr_n):
    if curr_t == 1: return curr_n
    if idx == len(P): return INF
    ans = bt(idx+1, curr_t, curr_n)
    if curr_t % (P[idx]-1) == 0:
        curr_t //= P[idx]-1
        curr_n *= P[idx]
        while curr_t%P[idx] == 0: curr_t //= P[idx]; curr_n *= P[idx]
        ans = min(ans, bt(idx+1, curr_t, curr_n))
    return ans
Z = bt(0, T, 1)
print(Z if Z < INF else -1)