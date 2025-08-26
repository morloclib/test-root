import sys

def morloc_fst(t):
    return t[0]

def morloc_ifelse(cond, x, y):
    if cond:
        return x
    else:
        return y

def morloc_eq(x, y):
    return x == y
