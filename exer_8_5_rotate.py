def rotate_word(word, n):
	"""rotate a given word with Caesar Cypher
	"""
	rotated = []
	for w in word:
		if w.isupper():
			wr = chr((ord(w) - ord('A') + n) % 26 + ord('A'))
			rotated.append(wr)
		if w.islower():
			wr = chr((ord(w) - ord('a') + n) % 26 + ord('a'))
			rotated.append(wr)


	return ''.join(rotated)


if __name__ == '__main__':
	assert(rotate_word('cheer', 7) == 'jolly')
	assert(rotate_word('melon', -10) == 'cubed')
	assert(rotate_word('IBM', -1) == 'HAL')