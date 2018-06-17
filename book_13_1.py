import string
from collections import Counter
import random
from bisect import bisect

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: file object
    """

    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_file(filename, skip_header=True):
    """Makes a histogram that is built from the words in a file

    filename: string
    skip_header: bool, whether to skip the Gutenberg header

    returns: map from each word to its frequencies
    """
    hist = dict()
    fp = open(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        hist = process_line(line, hist)

    return hist


def process_line(line, hist):
    """adds the words in the line to the given histogram, to update the histogram

    line: string
    hist: map from word to frequencies
    """

    hist_c = Counter(hist)

    # replace hyphens with spaces
    line = line.replace('-', ' ')
    strippables = string.punctuation + string.whitespace

    words = []
    for word in line.split():
        word = word.strip(strippables).lower()
        words.append(word)

    hist_c.update(words)
    return dict(hist_c)


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    c = Counter(hist)
    for word, count in c.most_common(num):
        print(word, count)


def total_words(hist):
    """returns the total number of words from a histogram

    hist: a map from words to their frequencies
    returns: int
    """
    return sum(hist.values())



def different_words(hist):
    return len(hist)


def subtract(d1, d2):
    '''returns all words that appear only in d1 but not in d2

    d1, d2: dictionary, map from words to their frequencies
    returns: set
    '''
    return set(d1) - set(d2)


def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.

    hist: map from word to frequency
    returns: a word
    """
    words = []
    freqs = []

    total_freq = 0 

    # make a list of words and a list of cumulative frequencies
    for word,freq in hist.items():
        words.append(word)
        toatal_freq += freq
        freqs.append(toatal_freq)


    # pick up a random value and find its right location in the list of cumulative frequencies
    r = random.randint(0, total_freq-1)

    index = bisect(freqs, r)

    return words[index]






if __name__ == '__main__':
    hist = process_file('emma.txt')
    #print(hist)
    print_most_common(hist,5)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    words = process_file('words.txt')
    print("The words in the book emma that aren't in the word list are:")
    diff = subtract(hist, words)
    print(diff)


















