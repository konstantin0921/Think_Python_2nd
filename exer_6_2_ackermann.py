def ack(m, n):
	"""Ackermann function

	if m = 0, then A(m, n) = n +1
	if m > 0 and n = 0, then A(m, n) = A(m-1, 1)
	if m > 0 and n > 0, then A(m, n) = A(m-1, A(m, n-1))
	"""
	if m == 0:
		return n + 1
	if m > 0 and n == 0:
		return ack(m-1, 1)
	if m > 0 and n > 0:
		return ack(m-1, ack(m, n-1))

if __name__ == '__main__':
	assert(ack(3, 4) == 125)

	ack(10,9)

