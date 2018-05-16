def is_palindrome(word):
	return word == word[::-1]

def is_magic_number(number):
	"""returns True when the following conditions are satisfied.
	1: the number has six digits
	2. originally, the last 4 digits are palindrome
	3. after increasing 1, the last 5 digits are palindrome
	4. after increasing 2, the middle 4 digits are palindrome
	5. after increasing 3, all 6 digits are palindrome
	"""
	n0 = str(number)
	n1 = str(number+1)
	n2 = str(number+2)
	n3 = str(number+3)
	if len(n0) == 6 and is_palindrome(n1[-4:]) and is_palindrome(n2[1:5]) and is_palindrome(n3):
		return True
	else:
		return False

def find_all_magic_number():
    i = 100000
    while i < 999997:
    	if(is_magic_number(i)):
    		print(i)
    	i += 1

if __name__ == '__main__':
	find_all_magic_number()