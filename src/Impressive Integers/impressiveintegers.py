n = int(input())
if n == 1: print('1 2 2\n B 0 0 U'); exit()
if n in (2, 3, 5): print('impossible'); exit()
if n%2:
    b = (n-4)//2; print(2, b, 2+2*b); print('B', 0, 2, 'U'); print('B', 0, 2+b, 'U'); print('B', 0, 2+b, 'D'); print('B', b, 2, 'U')
    for i in range(n-4): print('A', i//2*2, i%2*2, 'UD'[i%2])
else:
    print(1, n//2-1, n//2); print('B', 0, 1, 'U')
    for i in range(n-1): print('A', i//2, i%2, 'UD'[i%2])