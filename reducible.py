from collections import defaultdict

def make_word_dict(filename):
    '''read a word list and returns a dictionary from a given filename

    have to add single letter words and empty string to the dictionary
    '''
    d = dict()
    for line in open(filename):
        word = line.strip().lower()
        d[word] = None

    for letter in ['a', 'i', '']:
        d[letter] = None

    return d


def subwords(word, word_dict):
    '''returns children of word, deleting one letter from word
    can produce its children

    word: string
    word_dict: word dictionary
    returns: list of string
    '''
    res = []

    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in word_dict:
            res.append(child)
    return res


"""memo is a dictionary, which maps a word to a list of its reducible children
"""
memo = dict()



def is_reducible(word, word_dict):
    '''when a word is reducible, returns a list of its reducible children

    A word is reducible if it has at least one child which is reducible. The empty
     string is also reducible.

    word: string
    word_dict: dictionary with words as keys

    returns: list of strings
    '''

    if word in memo:
        return memo[word]
    
    if word == '':
        return ['']

    res = []
    for child in subwords(word, word_dict):
        if is_reducible(child, word_dict):
            res.append(child)

    # memorize the result
    memo[word] = res
    return res

    
def find_all_reducible(word_dict):
    """Checks all words in the word_dict; returns a list reducible ones.

    word_dict: dictionary with words as keys
    returns: a list of reducible words
    """
    res = []
    for word in word_dict:
        if is_reducible(word, word_dict):
            res.append(word)

    return res


def print_trace(word, word_dict):
    """Prints the sequence of words that reduces this word to the empty string.
    If there is more than one choice, it chooses the first one.

    word: string, a reducible word
    """
    if len(word) == 0:
        return 

    print(word, end=' ')
    t = is_reducible(word, word_dict)
    print_trace(t[0], word_dict)


def print_longest_words(word_dict):
    """find the longest reducible words and print the reduce trace for them

    word_dict: dictionary with all valid words as keys
    """

    all_reducible_words = find_all_reducible(word_dict)
    t = [(len(word), word) for word in all_reducible_words]
    t.sort(reverse=True)

    for length, word in t[:5]:
        print_trace(word, word_dict)
        print('\n')



if __name__ == '__main__':
    word_dict = make_word_dict('words.txt')
    #print(is_reducible('sprite', word_dict))
    all_reducible_words = find_all_reducible(word_dict)
    #print(all_reducible_words)

    #print_trace('sprite', word_dict)
    print_longest_words(word_dict)
