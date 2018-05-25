def histogram(s):
    """creates a histogram

    s: sequence, e.g. string
    returns: dict
    """
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def print_hist(h):
    """prints the histogram, each line with a key and corresponding value

    h: histogram
    returns: None
    """
    for k in h:
        print(k, h[k])

def reverse_lookup(d, v):
    """returns the first corresponding key in a dictionary for the given value

    d: dict
    v: value

    returns: key of dict
    """
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('value does not appear in the dictionary')


def invert_dict(d):
    """invert a dictionary

    d: dict
    returns: a new inverted dict, its key is the original value, and its value is a list
    """
    inverse = dict()
    for k in d:
        v = d[k]
        if v not in inverse:
            inverse[v] = [k]
        else:
            inverse[v].append(k)
    return inverse


known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]
    else:
        t = fibonacci(n-1) + fibonacci(n-2)
        known[n] = t
        return t




if __name__ == '__main__':
    h = histogram('brontosaurus')
    print_hist(h)

    hist = histogram('parrot')
    print_hist(invert_dict(hist))

    print(fibonacci(10))
