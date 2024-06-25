D, W, C = map(int, input().split())
while True:
    if (E:=min((W%C or C)/(L:=(W+C-1)//C*2-1), D)*L) > W: print(0); break
    D -= E/L; W -= E
    if D <= 0: print(W); break