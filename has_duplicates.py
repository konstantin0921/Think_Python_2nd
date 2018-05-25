def has_duplicates(t):
    """returns True when any element i t appears more than once

    t: list or string

    returns: bool
    """
    return len(set(t)) != len(t)

def has_duplicates2(t):
    """using dict"""
    d = dict()
    for i in t:
        if i in d:
            return True
        else:
            d[i] = None
    return False


if __name__ == '__main__':
    t = [1, 2, 3]
    print(has_duplicates(t))
    t.append(1)
    print(has_duplicates(t))

    t = [1, 2, 3]
    print(has_duplicates2(t))
    t.append(1)
    print(has_duplicates2(t))
