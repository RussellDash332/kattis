import sys; input = sys.stdin.readline
from math import *
K = [11, 101, 1001, 1111, 10001, 100001, 111111, 1000001, 1010101, 10000001, 11111111, 100000001, 1000000001, 1001001001, 1111111111]
D = [1, 2, 3, 1, 4, 5, 1, 6, 2, 7, 1, 8, 9, 3, 1]
for _ in range(int(input())):
    x = int(input()); Z = []
    for k, d in zip(K, D):
        h = x//gcd(x, k); t = (10**(d-1)+h-1)//h
        if h*t < 10**d: Z.append(lcm(x, k)*t)
    print(min(Z))