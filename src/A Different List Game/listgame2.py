x = int(input())
p, ans = 2, 0

def count(rem, to_use, hs):
    # The idea is to use this in order:
    # [a0, a0], [a0, a1], ..., [a0, av], [a1, a1], [a1, a2], ..., [av, av],
    # [a0, a0, a0], [a0, a0, a1], ...
    # and so on since we know [a0, a1, ..., av] is sorted
    
    # to_use is the array of the index, i.e. when trying [a1, a3], to_use = [1, 3]
    i = 1
    while i <= len(to_use) and to_use[-i] == len(rem) - 1:
        i += 1
    if i == len(to_use) + 1:
        to_use = [0] * i
    else:
        to_use[-i] += 1
        for j in range(-1, -i-1, -1):
            to_use[j] = to_use[-i]
        
    # If the current high score >= t / |to_use|, we won't get any higher anyways
    if hs >= sum(rem) // len(to_use):
        return hs
    
    # Apply to_use to remove the respective factors unless it fails
    nxt = rem.copy()
    for idx in to_use:
        if nxt[idx] == 0:
            nxt = []
            break
        nxt[idx] -= 1
    if nxt:
        hs = 1 + count(nxt.copy(), to_use.copy(), max(hs - 1, 0))
    
    # We have a new highscore, consider not using the combi and move on
    return count(rem, to_use.copy(), hs)

check = []
while p * p <= x:
    k = 0
    while x % p == 0:
        x //= p
        k += 1
    # Greedily take the prime numbers as a single y
    if k:
        ans += 1
    # Deal with the k - 1 exponents later
    if k > 1:
        check.append(k - 1)
    p += 1

if x != 1: # x is prime, extra y
    ans += 1

if check:
    ans += count(check, [len(check) - 1], 0)
print(ans)