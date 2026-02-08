P = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion']
def s(x):
    if x < 10: return [['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'][x]]
    if x < 20: return [['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'][x-10]]
    if x < 100: return [['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'][x//10]] + s(x%10)*(x%10>0)
    if x < 1000: return s(x//100) + ['hundred'] + s(x%100)*(x%100>0)
    for i in range(33, 0, -3):
        if x//10**i: return s(x//10**i) + [P[i//3]] + s(x%10**i)*(x%10**i>0)
for _ in range(int(input())): print(' '.join(s(int(input()))))