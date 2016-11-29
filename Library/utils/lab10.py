'''
Created on 6 ian. 2016

@author: Vlad
'''

def cocktailSort(L, cmpF = None, reverse = False):
    '''
    Cocktail Sort. Complexity O(n^2).
    '''
    if reverse == True:
        reverse = -1
    else:
        reverse = 1
    n = len(L)
    swaps = True
    while swaps:
        swaps = False
        for i in range(0, n-1, 1):
            if cmpF != None:
                if reverse * cmpF(L[i], L[i+1]) > 0:
                    L[i], L[i+1] = L[i+1], L[i]
                    swaps = True
            else:
                if reverse * (L[i] - L[i+1]) > 0:
                    L[i], L[i+1] = L[i+1], L[i]
                    swaps = True
        if not swaps:
            break
        for i in range(n-2, -1, -1):
            if cmpF != None:
                if reverse * cmpF(L[i], L[i+1]) > 0:
                    L[i], L[i+1] = L[i+1], L[i]
                    swaps = True
            else:
                if reverse * (L[i] - L[i+1]) > 0:
                    L[i], L[i+1] = L[i+1], L[i]
                    swaps = True
    return L

def combSort(L, cmpF = None, reverse = False):
    '''
    Comb Sort. Complexity O(?).
    '''
    if reverse == True:
        reverse = -1
    else:
        reverse = 1
    gap = len(L)
    shrink = 1.248
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap/shrink)) #gap is a non-zero natural number
        swaps = False
        for i in range(len(L)-gap):
            if cmpF != None:
                if reverse * cmpF(L[i] - L[i+gap]) > 0:
                    L[i], L[i+gap] = L[i+gap], L[i]
                    swaps = True
            else:
                if reverse * (L[i] - L[i+gap]) > 0:
                    L[i], L[i+gap] = L[i+gap], L[i]
                    swaps = True
    return L

def mySort(L, cmpF = None, reverse = False):
    '''
    Sort the elements in the list L
    Input: L (iterable data structure having n elements)
                L = [k1, k2, ..., kn], ki in R, i=1,n, n in N
           cmpF(a, b) - binary function that will be used for comparing elements ('<' will be used if None)
                should return -1 (negative) if a < b
                               0 (zero)     if a = b
                               1 (positive) if a > b
           reverse (boolean)
                if True, sort in reverse order
    Output: L' (list) a permutation of L having the elements sorted
        postcond: L'=[k1', k2', ..., kn'], ki' in R, i=1,n
    '''
    return cocktailSort(L, cmpF, reverse)

def myFilter(L, accF, attrib):
    '''
    Filter the elements in the list L
    Input: L (iterable data structure having n elements)
                L = [k1, k2, ..., kn], ki in R, i=1,n, n in N
           accF - unary acceptance function that will be used for filtering elements
           attrib - attribute
    Output: res (sublist of L)
                res = [ki | ki in L and accF(ki), i<=n]
    '''
    res = []
    for elem in L:
        if accF(elem, attrib):
            res.append(elem)
    return res

