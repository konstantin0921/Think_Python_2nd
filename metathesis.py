from anagram_sets import find_all_anagrams

def word_distance(word1, word2):
    """returns the number of differences between two words

    word1, word2: string
    return: int
    """
    assert(len(word1) == len(word2))
    count = 0
    for l1, l2 in zip(word1, word2):
        if l1 != l2:
            count += 1
    return count


def print_all_methathesis_pairs(d):
    '''prints all pairs of words that can be generated by swapping two letters

    d: map from word to all its anagrams
    '''
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_distance(word1, word2) == 2:
                    print(word1, word2)


if __name__ == '__main__':
    all_anagrams = find_all_anagrams('words.txt')

    print_all_methathesis_pairs(all_anagrams)


