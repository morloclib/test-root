import sys

def morloc_ifelse(cond, x, y):
    if cond:
        return x
    else:
        return y

def morloc_eq(x, y):
    return x == y

def morloc_le(x, y):
    return x <= y

def morloc_fst(t):
    return t[0]

def morloc_snd(t):
    return t[1]

def morloc_toFst(f, x):
    return (f(x), x)

def morloc_toSnd(f, x):
    return (x, f(x))

def morloc_fst3(t):
    return t[0]

def morloc_snd3(t):
    return t[1]

def morloc_thr3(t):
    return t[2]

def morloc_and(x, y):
    return x and y

def morloc_or(x, y):
    return x or y

def morloc_not(x):
    return (not x)
