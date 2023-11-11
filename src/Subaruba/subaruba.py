import sys; input = sys.stdin.readline
m = input()
for _ in range(int(input())):
    s = input().strip(); r = []
    if m[0] == 'D':
        for i in s:
            if i in 'aeiouy': r.append('ub'+i)
            elif i in 'AEIOUY': r.append('Ub'+i.lower())
            else: r.append(i)
    else:
        for i in s:
            if len(r) > 1 and r[-2] == 'u' and r[-1] == 'b': r.pop(), r.pop(), r.append(i+'@')
            elif len(r) > 1 and r[-2] == 'U' and r[-1] == 'b': r.pop(), r.pop(), r.append(i.upper()+'@')
            else: r.append(i)
    print(''.join(r).replace('@', ''))