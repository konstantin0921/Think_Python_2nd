def in_bisect(sorted_list, target):
    """returns True if the target value is in the list, otherwise returns False,
    the underlying algorithm is binary search

    sorted_list: a sorted list
    target: target value

    returns: bool
    """
    size = len(sorted_list)
    left = 0
    right = size - 1

    while left <= right:
        middle = (left + right) // 2
        #print('left -> %d \t right -> %d \t middle -> %d' % (left, right, middle))
        if target < sorted_list[middle]:
            right = middle-1
        elif target > sorted_list[middle]:
            left = middle+1
        else:
            return True


    return False
       


def in_bisect_recursive(sorted_list, target):
    if len(sorted_list) == 0:
        return False
    if len(sorted_list) == 1 and sorted_list[0] == target:
        return True
    if len(sorted_list) == 1 and sorted_list[0] != target:
        return False

    middle = len(sorted_list) // 2

    if target < sorted_list[middle]:
        return in_bisect_recursive(sorted_list[:middle], target)
    else:
        return in_bisect_recursive(sorted_list[middle:], target)


def make_word_list():
    """reads lines from a file

    returns: list of strings
    """
    result = []
    for line in open('words.txt'):
        word = line.strip()
        result.append(word)
    return result


if __name__ == '__main__':
    words = make_word_list()

    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect(words, word))

    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect_recursive(words, word))




