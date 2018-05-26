def most_frequent(text):
    """returns the frequencies of different letters in descending order
    text: string
    returns: list of letters
    """
    hist = make_histogram(text)
    t = []
    for ch, freq in hist.items():
        t.append((freq, ch))
    t.sort(reverse=True)

    return [ch for freq, ch in t]



def make_histogram(s):
    """creates a histogram

    s: sequence, e.g. string
    returns: dict
    """
    hist = dict()
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist

def read_text(filename):
    return open(filename).read()


if __name__ == '__main__':
    text = read_text('emma.txt')
    most_frequent_letters = most_frequent(text)
    print(most_frequent_letters)
