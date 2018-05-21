from in_list import in_bisect, make_word_list

def deinterlock(word):
    """devide a word into two parts

    word: string
    return tuple of words, (evens, odds)
    """
    odds = word[1::2]
    evens = word[::2]
    return evens, odds


def check_interlock(word, word_list):
    """checks whether a word is made of two interlocked words

    word: string
    word_list: list of strings 
    returns: bool
    """
    evens, odds = deinterlock(word)
    return in_bisect(word_list, evens) and in_bisect(word_list, odds)



def three_way_interlock(word, word_list):
    for i in range(3):
        sub_word = word[i::3]
        if not in_bisect(word_list, sub_word):
            return False
    return True


if __name__ == '__main__':
    word_list = make_word_list()

    print('interlocked words:')
    for word in word_list:
        if check_interlock(word, word_list):
            print(word, deinterlock(word))


    print('three ways interlocked words:')
    for word in word_list:
        if three_way_interlock(word, word_list):
            print(word, word[0::3], word[1::3], word[2::3])

