op = {'(': 1, '<': 2, '{': 3, '[': 4}
cl = {')': 1, '>': 2, '}': 3, ']': 4}
mem = {}
def bt(idx, p, t):
    k = (idx, p, t)
    if k in mem: return mem[k]
    if len(S)-idx < t: return 0
    if idx == len(S): return 1
    if S[idx] in '([<{': mem[k] = bt(idx+1, 5*p+op[S[idx]], t+1); return mem[k]
    if S[idx] in ')]>}':
        if p and p%5 == cl[S[idx]]: mem[k] = bt(idx+1, p//5, t-1); return mem[k]
        else: mem[k] = 0; return 0
    z = 0
    if p: z = bt(idx+1, p//5, t-1)
    for i in '([<{': z += bt(idx+1, 5*p+op[i], t+1)
    mem[k] = z; return z
S = input(); print(0 if len(S)%2 else bt(0, 0, 0))