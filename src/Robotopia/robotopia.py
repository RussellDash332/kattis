import sys

for line in sys.stdin:
    r = line.split()
    if len(r) == 6:
        a,d,b,e,c,f = map(int, r)
        # Basically ax + by = c and dx + ey = f
        sols = 0
        for x in range(1,max(c,f)+1):
            if c > a*x and f > d*x and (c-a*x) % b == 0 and (f-d*x) % e == 0: # exists an integer solution for both
                y = (c-a*x)//b # particular soln for the first eqn
                if y > 0 and d*x+e*y == f: # y is a solution for both
                    sols += 1
                    soln = (x,y)
        if sols == 1: print(f'{soln[0]} {soln[1]}')
        else: print("?")