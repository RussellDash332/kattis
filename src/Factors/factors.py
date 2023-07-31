primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
facts = [1, 1]
for i in range(63): facts.append(facts[-1]*(i+2))
nums = set()
def bt(exp=[0]*len(primes), v=1, idx=0):
    if idx != len(exp) and v < 2**63:
        if v > 1: nums.add((tuple(exp), v))
        if idx == 0 or exp[idx] < exp[idx-1]:
            exp[idx] += 1
            bt(exp.copy(), v*primes[idx], idx), bt(exp.copy(), v*primes[idx], idx+1)
bt()
h = {}
for e, n in nums:
    f = facts[sum(e)]
    for p in e: f //= facts[p]
    if f not in h or h[f] > n: h[f] = n

import sys
for l in sys.stdin: print(int(l), h[int(l)])