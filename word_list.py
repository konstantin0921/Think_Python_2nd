import time

def read_words(filename):
    """reads the given file of words

    filename: string

    returns: list of words
    """
    words = []
    for line in open(filename):
        words.append(line.strip())
    return words

def read_words_2(filename):
    words = []
    for line in open(filename):
        words = words + [line.strip()]
    return words

def read_words_3(filename):
    return [line.strip() for line in open(filename)]


def main():
    """compares the running time, which one takes shorter
    """
    filename = 'words.txt'

    start = time.time()
    t = read_words(filename)
    running_time = time.time() - start
    print(len(t))
    print(t[:10])
    print('running time is %f seconds using append' % running_time)

    start = time.time()
    t = read_words_2(filename)
    running_time = time.time() - start
    print(len(t))
    print(t[:10])
    print('running time is %f seconds using list +.' % running_time)

    start = time.time()
    t = read_words_3(filename)
    running_time = time.time() - start
    print(len(t))
    print(t[:10])
    print('running time is %f seconds using list comprehension' % running_time)




if __name__ == '__main__':
    """the winner will be list comprehension"""
    main()
