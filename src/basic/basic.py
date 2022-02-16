import sys
skip = input()

def parse(state):
    s = state.split('#')
    b = int(s[0])
    if 2 <= b <= 16:
        return str(int(s[1], int(s[0])))
    else:
        raise Exception

def check(query):
    if query != query.lower(): # '#'.islower() returns False
        return 'no'
    while True:
        k = query.find('##')
        if k == -1:
            break
        try:
            query = parse(query[:k+1]) + query[k+1:]
        except:
            return 'no'
    try:
        if query.count('#') == 0:
            try:
                test = int(query)
                return 'yes'
            except:
                return 'no'
        elif query.count('#') != 2:
            return 'no'
        query = parse(query)
        return 'yes'
    except:
        return 'no'

for line in sys.stdin:
    print(check(line.strip()))