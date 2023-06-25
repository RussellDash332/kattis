import sys, string
code = {}
for l in sys.stdin:
    pos = l.find(' ')
    code[int(l[:pos])] = l[pos+1:].strip()
code = sorted(code.items())
mapper, ptr, end, reg = {ln:i for i, (ln, _) in enumerate(code)}, 0, len(code), {i: 0 for i in string.ascii_uppercase}
def handle_of(res): return (res+2**31)%(2**32)-(2**31)
handle_op = {
    '+': lambda x,y: handle_of(x+y),    '-': lambda x,y: handle_of(x-y),
    '*': lambda x,y: handle_of(x*y),    '/': lambda x,y: handle_of(int(x/y)),
    '=': lambda x,y: x==y,              '<': lambda x,y: x<y,
    '>': lambda x,y: x>y,               '<=': lambda x,y: x<=y,
    '>=': lambda x,y: x>=y,             '<>': lambda x,y: x!=y
}
while ptr != end:
    nxt, cmd = ptr+1, code[ptr][1]
    pos = cmd.find(' ')
    kw = cmd[:pos]
    if kw == 'LET':
        a, _, *exp = cmd[pos+1:].split()
        if len(exp) == 1: reg[a] = int(reg[exp[0]] if exp[0].isupper() else exp[0])
        else:
            v1, op, v2 = exp
            reg[a] = handle_op[op](int(reg[v1] if v1.isupper() else v1), int(reg[v2] if v2.isupper() else v2))
    elif kw[0] == 'P':
        obj = cmd[pos+1:]
        print(obj[1:-1] if obj[0] == '"' else reg[obj], end='\n'*(kw[-1]=='N'))
    elif kw == 'IF':
        pos2 = cmd.find(' THEN GOTO')
        v1, op, v2 = cmd[pos+1:pos2].split()
        if handle_op[op](int(reg[v1] if v1.isupper() else v1), int(reg[v2] if v2.isupper() else v2)): nxt = mapper[int(cmd[pos2+11:])]
    ptr = nxt