ones = ['nul', 'en', 'to', 'tre', 'fire', 'fem', 'seks', 'syv', 'otte', 'ni', 'ti', 'elleve', 'tolv', 'tretten', 'fjorten', 'femten', 'seksten', 'sytten', 'atten', 'nitten']
tens = ['', '', 'tyve', 'tredive', 'fyrretyve', 'halvtredjesindstyve', 'tresindstyve', 'halvfjerdsindstyve', 'firsindstyve', 'halvfemsindstyve']
def spell(n):
    if n < 20: return ones[n]
    elif n < 100: return (ones[n%10]+'og')*(n%10>0)+tens[n//10]
    elif n < 1000:      t, u = divmod(n, 100);      m = spell(u)*(u>0); r = 'og'*('og' not in m and m>'')+m; s = spell(t); return ['et',s][t>1]+'hundred'+'e'*(t>1)+r
    elif n < 10**6:     t, u = divmod(n, 1000);     m = spell(u)*(u>0); r = 'og'*('og' not in m and m>'')+m; s = spell(t); return ['et',s][t>1].replace('ogen','oget')+'tusind'+r
    elif n < 10**9:     t, u = divmod(n, 10**6);    m = spell(u)*(u>0); r = 'og'*('og' not in m and m>'')+m; s = spell(t); return s+'million'+'er'*(t>1 and 'ogen' not in s)+r
    elif n < 10**12:    t, u = divmod(n, 10**9);    m = spell(u)*(u>0); r = 'og'*('og' not in m and m>'')+m; s = spell(t); return s+'milliard'+'er'*(t>1 and 'ogen' not in s)+r
    elif n < 10**15:    t, u = divmod(n, 10**12);   m = spell(u)*(u>0); r = 'og'*('og' not in m and m>'')+m; s = spell(t); return s+'billion'+'er'*(t>1 and 'ogen' not in s)+r
    elif n < 10**18:    t, u = divmod(n, 10**15);   m = spell(u)*(u>0); r = 'og'*('og' not in m and m>'')+m; s = spell(t); return s+'billiard'+'er'*(t>1 and 'ogen' not in s)+r
    return 'entrillion'
print(spell(int(input())))