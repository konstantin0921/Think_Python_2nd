from in_list import in_bisect, make_word_list


def reverse_pair(word, word_list):
    """checks whether a reversed word in the word_list

    word: string
    word_list: list of strings
    returns: bool
    """
    reversed_word = word[::-1]
    return in_bisect(word_list, reversed_word)

if __name__ == '__main__':
    words_list = make_word_list()

    for word in words_list:
        if reverse_pair(word, words_list):
            print(word, word[::-1])
