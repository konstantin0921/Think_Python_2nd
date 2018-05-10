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

def is_palindrome2(word):
	return word == word[::-1]


if __name__ == '__main__':
	assert(is_palindrome('redivider') is True)
	assert(is_palindrome2('redivider') is True)