def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def is_palindrome(word):
	if len(word) == 0:
		return True

	if len(word) == 1:
		return True

	return (first(word) == last(word)) and is_palindrome(middle(word))


if __name__ == '__main__':
	assert(is_palindrome('redivider') is True)