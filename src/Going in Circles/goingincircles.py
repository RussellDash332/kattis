from random import *
'''
If n >= L for some sufficiently big L, we can create a random string of length L, insert this string into the first L carriages, then go one full cycle hoping we will never see this random string again except the start.
Otherwise, we can insert L-1 zeroes and then insert 1, then find the number of loops to get 1 again since there will be exactly one 1.
'''
L = 18; p = [0]*(L-1)+[1]
for i in range(2*L):
    b = int(input())
    if b: print('? flip'); input()
    print('? left')
for i in range(2*L):
    b = int(input())
    print('? right')
for i in range(L):
    b = int(input())
    if b != p[i]: print('? flip'); input()
    print('? left')
for i in range(L):
    b = int(input())
    if b == 1: print('!', i+1), exit(0)
    print('? left')
p = [randint(0, 1) for _ in range(L)]; c = []
while p != c[-L:]:
    b = int(input())
    if len(c) < len(p) and p[len(c)] != b: print('? flip'); input()
    c.append(b); print('? left')
print('!', len(c)-L)