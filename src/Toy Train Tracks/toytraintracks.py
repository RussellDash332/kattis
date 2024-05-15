s, c = map(int, input().split()); s -= s%2; c -= c%2
if s == 0:
    c -= c%4
    if c <= 8: print('LLLL')
    elif c <= 12: print('LRRLRRLRRLRR')
    else: print(('RLRRLR'+'LR'*((c-12)//4))*2)
else:
    if c%4 == 0: print(('L'+'S'*(s//2)+'L'+'RL'*((c-4)//4))*2)
    else: print('LR'*((c-6)//4)+'L'+'S'*(s//2)+'LL'+'S'*(s//2-1)+'R'+'LR'*((c-6)//4)+'LLS')