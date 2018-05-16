def nested_sum(t):
    """returns sum of the nested integer list
    """
    return sum(list(flatten(t)))


def head(t):
        return t[0]

def tail(t):
    return t[1:]

def flatten(t):
    """flattens the nested list, returns a generator
    """
    if isinstance(t, list):
        for i in t:
            for element in flatten(i):
                yield element
    else:
        yield t

def cumsum1(t):
    """Computes the cumulative sum of the numbers in t."""
    result = []
    for i in range(len(t)):
        stop = i + 1
        accu = sum(t[:stop])
        result.append(accu)
    return result

def cumsum2_elem(t, pos):
    """recursive version 
    Computes the cumulative sum of the numbers from index zero to pos
    """
    if pos == 0:
        return t[0]
    else:
        return cumsum2_elem(t, pos-1) + t[pos]

def cumsum2(t):
    result = []
    i = 0 
    while i < len(t):
        result.append(cumsum2_elem(t, i))
        i += 1
    return result

def cumsum3_elem(t, pos, accu):
    """tail recursive """
    if pos == 0:
        return accu + t[0]
    else:
        return cumsum3_elem(t, pos-1, accu + t[pos])

def cumsum3(t):
    result = []
    i = 0 
    while i < len(t):
        result.append(cumsum3_elem(t, i, 0))
        i += 1
    return result



def middle(t):
    """Returns all but the first and last elements of t.

    t: list

    returns: new list
    """
    return t[1:-1]


def chop(t):
    """removes the first and last elements of t

    t: list

    returns: None
    """
    del t[0]
    del t[-1]

def is_sorted(t):
    """returns True when the list t is sorted 

    t: list

    returns: bool
    """
    i = 0
    while i < len(t)-1:
        if t[i] > t[i+1]:
            return False
        i += 1
    return True

def is_anagram(word1, word2):
    """Checks whether two words are anagrams

    returns: bool
    """
    return sorted(word1) == sorted(word2)

def has_duplicates(t):
    """returns True when any element i t appears more than once

    t: list or string

    returns: bool
    """
    return len(set(t)) != len(t)


if __name__ == "__main__":
    t = [[1,2], [3], [4,5,6]]
    assert(nested_sum(t) == 21)

    t = [1,2,3]
    assert(cumsum1(t) == [1, 3, 6])
    assert(cumsum2(t) == [1, 3, 6])
    assert(cumsum3(t) == [1, 3, 6])

    t = [1,2,3,4]
    assert(middle(t) == [2,3])

    t = [1,2,3,4]
    chop(t)
    assert(t == [2,3])

    assert(is_sorted([1, 2, 2]) is True)
    assert(is_sorted(['b', 'a']) is False)

    assert(has_duplicates('cba') is False)
    assert(has_duplicates('abba') is True)




