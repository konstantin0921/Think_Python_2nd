from book_dictionary import print_hist, histogram

def invert_dict(d):
    """invert a dictionary, using setdefault function from dict

    d: dict
    returns: a new inverted dict, its key is the original value, and its value is a list
    """
    rd = dict()
    for k in d:
        val = d[k]
        rd.setdefault(val, list()).append(k)
    return rd

if __name__ == '__main__':
    hist = histogram('parrot')
    print_hist(hist)
    print_hist(invert_dict(hist))