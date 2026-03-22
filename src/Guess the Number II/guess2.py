def ask(q): print('?', q); return input()
lo, hi = 0, 31
while hi-lo > 1:
    v = ask(2**(mi:=(lo+hi)//2)//2)
    if v == 'Too high!': hi = mi
    elif v == 'Too low!': lo = mi
    else: exit()
lo = 1<<lo-1 if lo else 0; hi = min(2*lo if lo else 1, 1e9)
while 1:
    v = ask(mi:=(lo+hi)/2)
    if v == 'Too high!': hi = mi
    elif v == 'Too low!': lo = mi
    else: exit()