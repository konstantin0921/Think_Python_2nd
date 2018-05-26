from pronounce import read_dictionary

def remove_first_letter(word):
    return word[1:]

def remove_second_letter(word):
    if len(word) != 0:
        return word[0] + word[2:]

def homophone_words(word_one, word_two, pron_dict):
    """returns True if the two words have same pronouciation

    word_one: string
    word_two: string
    pron_dict: dict
    returns: bool
    """
    if word_one not in pron_dict or word_two not in pron_dict:
        return False
    return pron_dict[word_one] == pron_dict[word_two]


def make_word_dict():
    """builds a word dictionary from words.txt, each word in the file is a key
    """
    d = dict()
    for line in open('words.txt'):
        word = line.strip().lower()
        d[word] = None

    return d


def is_magic_word(word, word_dict, pron_dict):
    """checks whether the word has following properties:
    removing the first letter yields a new word with the same pronunciation.
    removing the second letter yields a new word with the same pronunciation.
    word: string
    word_dict: dict, words as keys
    pron_dict: dict, words as keys, related pronunciation as values
    """
    word1 = remove_first_letter(word)
    word2 = remove_second_letter(word)
    if word1 not in word_dict or word2 not in word_dict:
        return False

    if not homophone_words(word, word1, pron_dict):
        return False

    if not homophone_words(word, word2, pron_dict):
        return False

    return True


if __name__ == '__main__':
    pro_dict = read_dictionary()
    word_dict = make_word_dict()

    for word in word_dict:
        if is_magic_word(word, word_dict, pro_dict):
            print(word, remove_first_letter(word), remove_second_letter(word))


