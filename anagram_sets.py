from collections import defaultdict

def agent(word):
    '''Returns the agent of the given word

    Agent is a string that has all the letters in order

    word: string
    returns: string
    '''
    t = list(word)
    t.sort()
    return ''.join(t)


def find_all_anagrams(filename):
    """Finds all anagrams from a list of words

    filename: the file contains a list of words

    returns: a map from an agent to all its anagrams
    """
    d = defaultdict(list)

    for line in open(filename):
        word = line.strip().lower()
        t = agent(word)
        d[t].append(word)

    return d


def print_anagram_sets(d):
    '''Prints the anagram in d

    d: a map from agents to list of their anagrams
    '''
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)


def print_anagrams_sets_in_descending_order(d):
    '''Prints the anagram in d with the longest first

    d: a map from agents to list of their anagrams
    '''
    t = [(len(v), k) for k, v in d.items() if len(v) > 1]

    t.sort(reverse=True)
    for length, k in t:
        print(length, d[k])


def filter_length(d, n):
    '''filter out only the words that have length n

    d: a map from agents to list of their anagrams
    n: length

    returns: new map from word to anagrams
    '''
    res = {k : v for k, v in d.items() if len(v) == n}
    return res


if __name__ == '__main__':
    assert(agent('hello') == 'ehllo')

    all_anagrams = find_all_anagrams('words.txt')

    #print_anagram_sets(all_anagrams)

    #print_anagrams_sets_in_descending_order(all_anagrams)

    eigth_letters = filter_length(all_anagrams, 8)

    print_anagram_sets(eigth_letters)

