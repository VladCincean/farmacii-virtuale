'''
Created on 7 dec. 2015

@author: Vlad Cincean
'''

def to_value(d):
    '''
    Converts a digit represented in any base (2, 3, ..., 10 or 16) to its decimal value
    Input: d (character) - the digit in any base
    Output: v (integer) - d's decimal value
    '''
    MAP = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    return MAP[str(d)]

def to_repr(v):
    '''
    Converts a decimal value (0, 1, ..., 15) to its representation in a numerical base (max 16)
    Input: v (integer) - the decimal value
    Output: d (character) - the representation in base 16 (or lower) of the given decimal value
    '''
    MAP = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
           10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    return MAP[int(v)]

def reverse(st):
    '''
    Returns the given string 'st' in the reverse order
    e.g. if st = 'abc12', then '21cba' is returned
    Input: st (string)
    Output: st2 (string)
    '''
    if st == "":
        return
    else:
        st2 = ""
        for i in range(len(st)-1, -1, -1):
            st2 += st[i]
        return st2
    
def check_representation(n, p):
    '''
    Checks if the a number is correctly represented in base p
    Input: n (string) - the representation in base p of a number
           p (integer) - the base (2, 3, ..., 10 or 16)
    Output: True, if the n is correctly represented in base p
            False, otherwise
    '''
    if len(n) == 0:
        return False
    
    ''' The list 'vector' stores all the possible correct digits characteristic to base 16 (or other pase p < 16) '''
    vector = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for i in range(0, len(n), 1):
        if n[i] not in vector[:p]:
            return False
    return True
    