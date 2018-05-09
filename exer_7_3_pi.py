import math
def factorial(n):
	if n < 0:
		print('n must be a positive number')
		return None
	if n == 0:
		return 1
	return n * factorial(n-1)


def estimate_pi():
	k = 0
	total = 0
	factor = 2 * math.sqrt(2) / 9801
	while True:
		numerator = factorial(4*k) * (1103 + 26390*k)
		denominator = factorial(k)**4 * (396)**(4*k)
		item = numerator / denominator
		if abs(item) < 1e-15: 
			break
		total += item
		k += 1

	return 1 / (factor * total)

if __name__ == '__main__':
	epsilon = 0.000001
	assert(abs(estimate_pi() - math.pi) < epsilon)
	print(estimate_pi())

