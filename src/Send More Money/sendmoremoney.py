# /greatswercporto
def check_back(exp, assgn, carry):
    try:
        d = carry
        for i in exp[:-1]:
            if i:
                d += assgn[i[-1]]
        e = assgn[exp[-1][-1]]
        return (d % 10 == e % 10, d//10)
    except:
        return False

def backtrack(exp, domains, assgn, carry=0):
    for i in leads:
        if i in assgn and assgn[i] == 0:
            return
    if not any(exp) and carry == 0:
        mem.add(tuple(sorted(assgn.items())))
        return
    t = check_back(exp, assgn, carry)
    if not (type(t) == tuple and not t[0]):
        if t != False:
            exp = list(map(lambda x: x[:-1], exp))
            carry = t[1]
            if not any(exp[:-1]) and exp[-1] and carry:
                if exp[-1][-1] in assgn and assgn[exp[-1][-1]] == carry:
                    mem.add(tuple(sorted(assgn.items())))
                    return
                if exp[-1][-1] not in assgn and carry in domains:
                    mem.add(tuple(sorted(list(assgn.items()) + [(exp[-1][-1], carry)])))
                    return
        if not any(exp) and not carry:
            mem.add(tuple(sorted(assgn.items())))
            return
        rec = False
        for i in {i[-1] for i in exp if i}:
            if i not in assgn:
                rec = True
                for domain in sorted(domains):
                    assgn[i] = domain
                    domains -= {assgn[i]}
                    backtrack(exp, domains, assgn, carry)
                    domains.add(assgn[i])
                    del assgn[i]
                break
        if t != False and not rec:
            backtrack(exp, domains, assgn, carry)
    return

l, r = input().split('='); a, b = l.split('+'); letters = {*a, *b, *r}; exp = ([*a], [*b], [*r]); mem = set()
leads = {i[0] for i in exp}; backtrack(exp, set(range(10)), {})
if not mem: print('impossible'), exit(0)
asg = dict(min(mem))
for i in exp:
    for j in range(len(i)):
        try: i[j] = str(asg[i[j]])
        except: print('impossible'), exit(0)
print(''.join(exp[0])+'+'+''.join(exp[1])+'='+''.join(exp[2]))