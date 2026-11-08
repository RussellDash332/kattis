import sys; input = sys.stdin.readline
T = 0
while (S:=int(input())):
    T += 1; C = t = c = 0
    print(f'Output for data set {T}, {S} bytes:')
    while C < S:
        s = int(input()); C += s; t += 1; c += s
        if t%5<1:
            if not c: print('   Time remaining: stalled')
            else: print('   Time remaining:', ((S-C)*5+c-1)//c, 'seconds')
            c = 0
    print('Total time:', t, 'seconds')