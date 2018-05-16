def has_no_e(word):
	"""returns True is the word doesn't have 'e'
	"""
	for w in word:
		if w == 'e':
			return False
	return True

def avoids(word, forbidden):
	"""returns True if the word has no forbidden characters
	"""
	for w in word:
		if w in forbidden:
			return False
	return True

def uses_only(word, available):
	"""returns True if the word only has available characters
	"""
	for w in word:
		if w not in available:
			return False
	return True

def uses_all(word, required):
	"""returns True if all required characters appear at least once in the word
	"""
	for req in required:
		if req not in word:
			return False
	return True

def is_abecedarian(word):
	"""returns True if the letters in a word appear in alphabetical order (double letters are okay)
	"""
	if len(word) <= 1:
		return True
	if word[0] > word[1]:
		return False
	return is_abecedarian(word[1:])

def is_triple_double(word):
	"""returns True if the word contains three consecutive double letters.
	For example, the word committee, c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ that sneaks in there. 
	Or Mississippi: M-i-s-s-i-s-s-i-p- p-i. If you could take out those i’s it would work.

	word: string
	return: bool
	"""
	i = 0
	total = 0
	while i < len(word)-1:
		if word[i] == word[i+1]:
			total += 1
			if total == 3:
				return True
			i += 2
		else:
			# reset total to zero
			total = 0
			i += 1
	return False


def find_triple_double():
	"""finds all triple double words from the given text.
	"""
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		if is_triple_double(word):
			print(word)




if __name__ == '__main__':
	find_triple_double()
	