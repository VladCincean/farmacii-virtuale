'''
Created on 7 dec. 2015

@author: Vlad Cincean
'''
from math import log2

def to_base_2(n, s):
    '''
    Performs a rapid conversion from base p to base 2
    Input: n (string) - the number's representation in base s to convert
           s (integer) - the source base (can be 4, 8 or 16)
    Output: out (string) - the representation in base 2 of the number
    '''
    if s != 2 and s != 4 and s != 8 and s != 16:
        raise ValueError("Error! Cannot perform a rapid conversion from the source base " + str(s))
    MAP = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111',
           '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
    ''' we compute the result '''
    out = ''
    for digit in n:
        out += MAP[digit][-int(log2(s)):]
    ''' we remove the insignificant zeros from the front of the result '''
    while len(out) > 1 and out[0] == '0':
        out = out[1:]
    return out

def from_base_2(n, d):
    '''
    Performs a rapid conversion from base 2 to base d
    Input: n (string) - the number's representation in base 2 to convert
           d (integer) - the destination base (can be 4, 8 or 16)
    Output: out (string) - the representation in base d of the number
    '''
    if d != 2 and d != 4 and d != 8 and d != 16:
        raise ValueError("Error! Cannot perform a rapid conversion to the destination base " + str(d))
    MAP = {'0000':'0', '0001':'1', '0010':'2', '0011':'3', '0100':'4', '0101':'5', '0110':'6', '0111':'7',
           '1000':'8', '1001':'9', '1010':'A', '1011':'B', '1100':'C', '1101':'D', '1110':'E', '1111':'F'}
    ''' we add insignificant zeros in the front of the number's representation in base 2 '''
    while len(n)%int(log2(d)) != 0:
        n = '0' + n
    ''' we compute the result '''
    out = ''
    for i in range(0, len(n), int(log2(d))):
        out += MAP[(4-int(log2(d)))*'0' + n[i:i+int(log2(d))]]
    ''' we remove the insignificant zeros from the front of the result '''
    while len(out) > 1 and out[0] == '0':
        out = out[1:]
    return out

def rapid_convert(n, s, d):
    '''
    Performs a rapid conversion between two bases as powers of 2 (2, 4, 8 or 16)
    Input: n (string) - the number's representation in base s
           s (integer) - the source base
           d (integer) - the destination base
    Output: out (string) - the representation in base d of the number
    '''
    out = from_base_2(to_base_2(n, s), d)
    return out
        