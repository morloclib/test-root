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

# nothing a :: Maybe a
morloc_nothing = None

# just a :: a -> Maybe a
def morloc_just(x):
    return x

# fromJust a :: Maybe a -> a -- unsafe, undefined for Nothing
def morloc_fromJust(x):
    if x is not None:
        return x
    else:
        raise ValueError("in fromJust, value must not be None")

#  isNothing a :: Maybe a -> Bool
def morloc_isNothing(x):
    return x is None

def morloc_add(x, y):
    return x + y

def morloc_sub(x, y):
    return x - y

#  fold f a b :: (b -> a -> b) -> b -> f a -> b
def morloc_fold(fbab, b, fa):
    for x in fa:
        b = fbab(b, x)
    return b

def morloc_map_list(f, xs):
    return list(map(f, xs))

def morloc_at(i, xs):
    return xs[i]

def morloc_slice(i, j, xs):
    return xs[i:j]
