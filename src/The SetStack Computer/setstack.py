import sys
t = int(input())
mem = {(): 0, (0,): 1, (0, 0): 2, (1,): 3}
rev = [(), (0,), (0, 0), (1,)]

def parse(ss):
    ss = tuple(sorted(set(ss)))
    if ss in mem: return mem[ss]
    ns = tuple(parse(i) if type(i) != int else i for i in ss)
    mem[ns] = len(mem); rev.append(ns)
    return mem[ns]

for l in sys.stdin:
    try:
        n, stack = int(l), []
        if n == 0: print('***'); n = -1
    except:
        c = l.strip()
        if c == 'PUSH': stack.append(0)
        elif c == 'DUP': stack.append(stack[-1])
        else:
            a, b = stack.pop(), stack.pop()
            if c == 'ADD':      stack.append(parse(rev[b] + (a,)))
            elif c == 'UNION':  stack.append(parse(rev[b] + rev[a]))
            else:               a, b = rev[a], rev[b]; stack.append(parse([i for i in a if i in b]))
        n -= 1
        print(len(rev[stack[-1]]))
        if n == 0: print('***')