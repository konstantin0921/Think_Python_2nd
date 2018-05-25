from in_list import in_bisect, make_word_list
import time

def in_list_hashtable(word, words_dict):
    """returns true if the word is a key in the words_dict

    word: string
    words_dict: dict 
    returns: bool
    """
    return word in words_dict



def in_list(word, words_list):
    return word in words_list


def make_word_dict():
    words_dict = dict()
    for line in open('words.txt'):
        word = line.strip()
        if word not in words_dict:
            words_dict[word] = None
    return words_dict


if __name__ == '__main__':
    words_list = make_word_list()
    words_dict = make_word_dict()

    start = time.time()
    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_list(word, words_list))
    print('in_list running time is', time.time() - start)

    start = time.time()
    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect(words_list, word))
    print('in_list_binary_search running time is', time.time() - start)

    start = time.time()
    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_list_hashtable(word, words_dict))
    print('in_list_hashtable running time is', time.time() - start)   



