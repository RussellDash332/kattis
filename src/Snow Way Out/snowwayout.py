def ask(x, y): print(x, y, '?'); return input()[0]
print('3 3 .'); v = ask(6, 3)
if v == 'C':
    if (v:=ask(q:=8, 3)) == 'S': X = 7
    elif v == 'F': X = 6-(ask(q:=3, 3)=='C')
    else: X = 8+(ask(q:=9, 3)=='C')
else:
    if (v:=ask(q:=0, 3)) == 'S': X = 3
    elif v == 'F': X = 4
    elif (v:=ask(q:=2, 3)) == 'S': X = 1
    elif v == 'F': X = 0
    else: X = 2
if ask(q, 6) == 'C':
    if (v:=ask(q, 8)) == 'S': Y = 7
    elif v == 'F': Y = 6-(ask(q, 3)=='C')
    else: Y = 8+(ask(q, 9)=='C')
else:
    if (v:=ask(q, 0)) == 'S': Y = 3
    elif v == 'F': Y = 4
    elif (v:=ask(q, 2)) == 'S': Y = 1
    else: Y = 2*(v!='F')
print(X, Y, '!')