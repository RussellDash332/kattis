import sys
for l in sys.stdin:
    l = [*l.strip()]
    if len(l) == 1: break
    l[-2] = l[-1]; l.pop()
    o = l.copy()
    # work from the last digit
    pos = len(l)-1; found = False
    while pos >= 0:
        for d in range(ord(l[pos])-47, 10): # check if there is any digit larger than l[pos]
            for k in range(pos, len(l)):
                if ord(l[k]) == d+48 or (l[k] == '2' and d == 5) or (l[k] == '6' and d == 9) or (l[k] == '5' and d == 2) or (l[k] == '9' and d == 6): # found a digit higher than l[pos]
                    found = True; l[k] = l[pos]; l[pos] = str(d); break
            if found: break
        if found: break
        pos -= 1
    if not found: print('The price cannot be raised')
    else:
        l[pos+1:] = sorted(map(lambda x: '2' if x == '5' else '6' if x == '9' else x, l[pos+1:]))
        l.append('.'); l[-1], l[-2] = l[-2], l[-1]
        print(''.join(l))