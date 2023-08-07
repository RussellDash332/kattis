from itertools import permutations
ops = '+-*/'
a, b, c, d = map(int, input().split())

def gen(a, op1, b, op2, c, op3, d):
    return [
        ['(', a, op1, b, ')', op2, '(', c, op3, d, ')'],
        ['(', a, op1, b, op2, c, ')', op3, d],
        [a, op1, '(', b, op2, c, op3, d, ')'],
        ['(', a, op1, b, ')', op2, c, op3, d],
        [a, op1, b, op2, '(', c, op3, d, ')'],
        ['(', '(', a, op1, b, ')', op2, c, ')', op3, d],
        ['(', a, op1, '(', b, op2, c, ')', ')', op3, d],
        [a, op1, '(', '(', b, op2, c, ')', op3, d, ')'],
        [a, op1, '(', b, op2, '(', c, op3, d, ')', ')'],
        [a, op1, '(', b, op2, c, ')', op3, d],
        [a, op1, b, op2, c, op3, d]
    ]

pre = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
def check(exp):
    s = []; pf = []
    for i in ['(', *exp, ')']:
        if type(i) == int: pf.append(i)
        elif i == '(': s.append(i)
        elif i == ')':
            while s and s[-1] != '(': pf.append(s.pop())
            if not s or s[-1] == '(': s.pop()
        else:
            while s and pre[i] <= pre[s[-1]]: pf.append(s.pop())
            s.append(i)
    for i in pf:
        if type(i) == int: s.append(i)
        else:
            b, a = s.pop(), s.pop()
            if i == '+': s.append(a+b)
            elif i == '-': s.append(a-b)
            elif i == '*': s.append(a*b)
            elif i == '/':
                if b and a % b == 0: s.append(a//b)
                else: return False
    return s.pop() == 24

zero = {(a, b, c, d)}
one = {(b, a, c, d), (a, c, b, d), (a, b, d, c)} - zero
two = {(a, c, d, b), (a, d, b, c), (b, a, d, c), (b, c, a, d), (c, a, b, d)} - zero - one
three = {(a, d, c, b), (b, c, d, a), (b, d, a, c), (c, a, d, b), (c, b, a, d), (d, a, b, c)} - zero - one - two
four = {(b, d, c, a), (c, b, d, a), (c, d, a, b), (d, a, c, b), (d, b, a, c)} - zero - one - two - three
five = {(c, d, b, a), (d, b, c, a), (d, c, a, b)} - zero - one - two - three - four
six = {(d, c, b, a)} - zero - one - two - three - four - five
sets = [*enumerate((zero, one, two, three, four, five, six))]
def grade(exp):
    g = exp.count('(')
    nums = tuple(i for i in exp if type(i) == int)
    for i, s in sets:
        if nums in s: return g+2*i

best = 1e9
for aa, bb, cc, dd in set(permutations([a, b, c, d])):
    for op1 in ops:
        for op2 in ops:
            for op3 in ops:
                for exp in gen(aa, op1, bb, op2, cc, op3, dd):
                    if check(exp): best = min(best, grade(exp))
print(best if best<1e9 else 'impossible')