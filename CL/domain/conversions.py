'''
Created on 7 dec. 2015

@author: Vlad Cincean
'''
from domain.operations import add, mul, div

def substitution_method(n, s, d):
    '''
    Performs a conversion from base s to base d using the substitution method
    It is recommended if s < d ! Raises ValueError if s >= d or s,d not in {2, 3, ..., 10, 16}
    Input: n (string) - the number's representation in base s
           s (integer) - the source base
           d (integer) - the destination base)
    Output: res (string) - the number's representation in base d
    '''
    if s >= d or not(s >= 2 and s <= 10 or s == 16) or not(d >= 2 and d <= 10 or d == 16):
        raise ValueError("Cannot convert using substitution method!")
    ''' if s < d, then all the digits of the number's representation in base s are the same with those read in base d '''
    ''' if s < d, then s(d) = s (the source base represented in the destination base) '''
    ''' we compute the result '''
    res = '0'
    for i in range(len(n)-1, -1, -1):
        t = '1'
        for j in range(0, len(n)-1-i, 1):
            if s == 10:
                t = mul(t, 'A', d)
            else:
                t = mul(t, str(s), d)
        t = mul(t, n[i], d)
        res = add(res, t, d)
    ''' we return the result '''
    return res

def successive_divisions_method(n, s, d):
    '''
    Performs a conversion from base s to base d using the successive divisions method
    It is recommended if s > d ! Raises ValueError if s <= d or s,d not in {2, 3, ..., 10, 16}
    Input: n (string) - the number's representation in base s
           s (integer) - the source base
           d (integer) - the destination base)
    Output: out (string) - the number's representation in base d
    '''
    if s <= d or not(s >= 2 and s <= 10 or s == 16) or not(d >= 2 and d <= 10 or d == 16):
        raise ValueError("Cannot convert using successive divisions method!")
    
    q = n
    res = ''
    while q != '0':
        if d == 10:
            q, r = div(q, 'A', s)
        else:
            q, r = div(q, str(d), s)
        res = r + res
    ''' we delete the insignificant zeros from the front of the result, if necessary '''
    while len(res) > 0 and res[0] == '0':
        res = res[:-1]
    ''' we return the result '''
    return res
    
    
    