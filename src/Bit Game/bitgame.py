from random import *
def bt(v, b):
    if b == 20: print('?', v); return int(input())
    r = randint(0, 1)
    for i in (0, 1):
        if not bt(2*v+(i^r), b+1): return 1
    return 0
print('!', ['bob', 'alice'][bt(0, 0)])