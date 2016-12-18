'''
Created on 30 nov. 2015

@author: Vlad Cincean
'''
from utils.utils import to_value, to_repr, reverse

def add(a, b, p):
    '''
    Adds 2 numbers in base p
    Input: a (string) - the augend's representation in base p
           b (string) - the addend's representation in base p
           p (integer) - the base (2, 3, ..., 10 or 16)
    Output: c (string) - the representation in base p of the result of the multiplication
                c = a + b
    '''
    '''1. we reverse the order of the digits in both numbers' representations '''
    a = reverse(a)
    b = reverse(b)
    '''2. we add insignificant zeros where it is needed '''
    if len(a) > len(b):
        a += '0'
        while len(a) > len(b):
            b += '0'
    elif len(a) < len(b):
        b += '0'
        while len(a) < len(b):
            a += '0'
    elif len(a) == len(b):
        a += '0'
        b += '0'
    '''3. we initialize a 'transport string', which will store the transport digits for all addition iterations '''
    t = '0' #the first transport digit is '0' (zero)
    '''4. the addition process '''
    c = ''
    for i in range(0, len(a), 1):
        s = to_value(a[i]) + to_value(b[i]) + int(t[i])
        t += str(s // p) #it can be '0' or '1'
        c += to_repr(s % p)
    '''5. we remove the insignificant zero from the front of the result's representation in base p, if necessary '''
    while c[-1] == '0' and len(c) > 1:
        c = c[:-1]
    '''6. we reverse back the order of the digits in the result's representation '''
    c = reverse(c)
    '''7. we return the result '''
    return c

def sub(a, b, p):
    '''
    Subtracts 2 numbers in base p
    Input: a (string) - the minuend's representation in base p
           b (string) - the subtrahend's representation in base p
               condition: a >= b
               - returns ValueError in case this condition is not meet
           p (integer) - the base (2, 3, ..., 10 or 16)
    Output: c (string) - the representation in base p of the result of subtraction
                c = a - b
    '''
    '''1. we reverse the order of the digits in both numbers' representations '''
    a = reverse(a)
    b = reverse(b)
    '''2. we add insignificant zeros where it is needed '''
    while len(b) < len(a):
        b += '0'
    '''3. we initialize a 'transport string', which will store the transport digits for all subtraction iterations '''
    t = '0' #the first transport digit is '0' (zero)
    '''4. the subtraction process '''
    c = ''
    for i in range(0, len(a), 1):
        if to_value(a[i]) - int(t[i]) < to_value(b[i]):
            t += '1'
        else:
            t += '0'
        s = p*int(t[i+1]) + to_value(a[i]) - int(t[i]) - to_value(b[i])
        c += to_repr(s)
    '''5. we remove the insignificant zeros from the front of the result's representation in base p, if necessary '''
    while c[-1] == '0' and len(c) > 1:
        c = c[:-1]
    '''6. we reverse back the order of the digits in the result's representation '''
    c = reverse(c)
    '''7. we return the result '''
    return c

def mul(A, b, p):
    '''
    Multiplies a number A in base p by a digit b in base p
    Input: A (string) - the number's representation in base p
           b (character) - the digit's representation in base p
           p (integer) - the base (2, 3, ..., 10 or 16)
    Output: c (string) - the representation in base p of the result of the multiplication
                c = A * b
    '''
    '''1. we reverse the order of the digits in the number's representations '''
    A = reverse(A)
    '''2. we add a insignificant zero in the front of A's representation in base p '''
    A += '0'
    '''3. we initialize a 'transport string', which will store the transport digits for all multiplication iterations '''
    t = '0' #the first transport digit is '0' (zero)
    '''4. the multiplication process '''
    c = ''
    for i in range(0, len(A), 1):
        s = to_value(A[i]) * to_value(b) + to_value(t[i])
        t += to_repr(s // p)
        c += to_repr(s % p)
    '''5. we remove the insignificant zero from the front of the result's representation in base p, if necessary '''
    while c[-1] == '0' and len(c) > 1:
        c = c[:-1]
    '''6. we reverse back the order of the digits in the result's representation '''
    c = reverse(c)
    '''7. we return the result '''
    return c

def div(A, b, p):
    '''
    Divides a number A in base p by a digit b in base p
    Input: A (string) - the divident's representation in base p
           b (character) - the digit's representation in base p
               b <> 0
           p (integer) - the base (2, 3, ..., 10 or 16)
    Output: q (string) - the representation in base p of the quotient of the division
            r (character) - the representation in base p of the remainder of the division
                q remainder r = A / b
    '''
    if b == '0':
        raise ValueError("Cannot divide by zero!")
    
    '''1. we initialize a 'transport string', which will store the transport digits for all division iterations '''
    t = '0' #the first transport digit is '0' (zero)
    '''2. the division process '''
    q = ''
    for i in range(0, len(A), 1):
        q += to_repr((int(t[i]) * p + to_value(A[i])) // to_value(b))
        t += str((int(t[i])*p+to_value(A[i]))-(((int(t[i])*p+to_value(A[i])))//to_value(b))*to_value(b))
    r = t[-1]
    '''3. we remove the insignificant zero from the front of the quotient's representation in base p, if necessary'''
    while len(q) > 1 and q[0] == '0':
        q = q[-len(q)+1:]
    '''4. we return the result '''
    return q, r


    