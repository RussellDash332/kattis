import sys
input = sys.stdin.readline
for _ in range(int(input())):
    stack = []
    for _ in range(int(input())):
        c = input().strip()
        if c == 'PUSH':     stack.append(frozenset())
        elif c == 'DUP':    stack.append(stack[-1])
        else:
            a, b = stack.pop(), stack.pop()
            if c == 'ADD':      stack.append(b | {hash(a)})
            elif c == 'UNION':  stack.append(a | b)
            else:               stack.append(a & b)
        print(len(stack[-1]))
    print('***')