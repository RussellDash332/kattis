import sys; input = sys.stdin.readline
for _ in range(int(input())):
    n, arr = int(input()), [*map(int, input().split())]
    s = 0
    while True:
        # Find first unsorted position
        i = 1
        while i < n:
            if arr[i] < arr[i-1]: break
            i += 1
        if i == n: break
        c, d = 1, 2
        '''
        To move 6 from [1, 1, 2, 3, 4, 5, 9, 6] to the back need 48 steps = 3 * 2 * 2 * 2
        This suggests duplicate adds 1 to the multiplier :)
        '''
        for j in range(i):
            if arr[j] < arr[i]:
                if arr[j] == arr[j+1]: d += 1
                else: c *= d; d = 2
            else: break
        s += c
        # Propagate changes
        t = arr[i]
        for k in range(i-1, j-1, -1): arr[k+1] = arr[k]
        arr[j] = t
    print(s)