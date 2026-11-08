while 1:
    g, e, c, t = map(int, input().split())
    if g+e+c+t<1: break
    g = ~-g//t+1; e = ~-e//t+1
    if c == 3: p = g/(g+e)
    else: r = c/(6-c); p = 1-(1-r**e)/(1-r**(g+e))
    print('%.1f'%(p*100))