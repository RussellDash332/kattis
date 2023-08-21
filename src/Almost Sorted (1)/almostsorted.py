import sys; input = sys.stdin.readline
N, A, Q = int(input()), [*map(int, input().split())], int(input())
RS = {e:i for i,e in enumerate(sorted(A))}
i = 0
while A[RS[Q]] != Q:
    '''
    4 3 5 10 12 6 8 7 11 1 9 2
    10 3 5 4 12 6 8 7 11 1 9 2 -> 4 is now sorted
    1 3 5 4 12 6 8 7 11 10 9 2 -> 10 is now sorted
    '''
    while i < N and i == RS[A[i]]: i += 1
    if i == N: break
    pos = RS[A[i]]; A[i], A[pos] = A[pos], A[i]
print(*A)